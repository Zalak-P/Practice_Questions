class BankingSystem:

    def __init__(self):
        self.accounts = {}
        self.scheduled = []
        self.cashbacks = []
        self.payment_history = {}  # permanent payment records
        self.payment_counter = 1

    def process_cashback(self, timestamp):
        remaining = []

        for cashback in self.cashbacks:
            if cashback["payment_id"] not in self.payment_history:
                continue
            if cashback["execute_at"] <= timestamp:
                if cashback["target"] in self.accounts and cashback["payment_id"] in self.payment_history:
                    self.accounts[cashback["target"]]["balance"] += cashback["amount"]
                    self.payment_history[cashback["payment_id"]]["status"] = "cashback_completed"
            else:
                remaining.append(cashback)
        self.cashbacks = remaining

    def process_scheduled(self, timestamp):
        remaining = []
        self.scheduled.sort(key=lambda x: (x["execute_at"], x["payment_id"]))
        for scheduled in self.scheduled:
            if scheduled["execute_at"] <= timestamp:
                if scheduled["source"] not in self.accounts:
                    continue
                if scheduled["target"] not in self.accounts:
                    continue
                if scheduled["source"] == scheduled["target"]:
                    continue
                if scheduled["amount"] > self.accounts[scheduled["source"]]["balance"]:
                    continue
                self.accounts[scheduled["source"]]["balance"] -= scheduled["amount"]
                self.accounts[scheduled["target"]]["balance"] += scheduled["amount"]
                self.accounts[scheduled["source"]]["outgoing"] += scheduled["amount"]
                self.payment_history[scheduled["payment_id"]]["status"] = "executed"

                cashback_at = scheduled["execute_at"] + 86400000
                cashback = (scheduled["amount"] * 2) // 100
                self.cashback_details = {
                "target" : scheduled["source"],
                "amount" : cashback,
                "execute_at": cashback_at,
                "payment_id": scheduled["payment_id"]
                }
                self.cashbacks.append(self.cashback_details)
            else:
                remaining.append(scheduled)

        self.scheduled = remaining 

    def create_account(self, timestamp: int, account_id: str) -> bool:
        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)

        if account_id in self.accounts:
            return False

        self.accounts[account_id] = {
            "balance": 0,
            "outgoing": 0
        }
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int):
        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)

        if account_id not in self.accounts:
            return None

        self.accounts[account_id]["balance"] += amount
        return self.accounts[account_id]["balance"]

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int):
        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)

        if source_account_id not in self.accounts:
            return None

        if target_account_id not in self.accounts:
            return None

        if source_account_id == target_account_id:
            return None

        if self.accounts[source_account_id]["balance"] < amount:
            return None

        self.accounts[source_account_id]["balance"] -= amount
        self.accounts[target_account_id]["balance"] += amount
        self.accounts[source_account_id]["outgoing"] += amount

        return self.accounts[source_account_id]["balance"]

    def top_spenders(self, timestamp: int, n: int):
        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)

        sorted_res = sorted(
            self.accounts.items(),
            key=lambda x: (-x[1]["outgoing"], x[0])
        )
        result = []
        for key, value in sorted_res[:n]:
            result.append(f"{key}({value})")
        return result
    
    def schedule_payment(self, timestamp, src, dst, amount, delay):
        execute_at = timestamp + delay

        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)
        payment_id = f"payment{self.payment_counter}"
        self.payment_counter += 1

        self.scheduled.append({
            "payment_id": payment_id,
            "source": src,
            "target": dst,
            "amount": amount,
            "execute_at": execute_at
        })
        self.payment_history[payment_id] = {
            "source": src,
            "target": dst,
            "amount": amount,
            "status": "pending"        
        }
        return payment_id
    
    def payment_status(self, timestamp, payment_id):
        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)

        if payment_id not in self.payment_history:
            return "none"

        return self.payment_history[payment_id]["status"]

    def merge_accounts(self, timestamp, from_id, to_id):

        self.process_scheduled(timestamp)
        self.process_cashback(timestamp)

        if from_id not in self.accounts:
            return False

        if to_id not in self.accounts:
            return False

        if from_id == to_id:
            return False

        self.accounts[to_id]["balance"] += self.accounts[from_id]["balance"]
        self.accounts[to_id]["outgoing"] += self.accounts[from_id]["outgoing"]

        for scheduled in self.scheduled:
            if scheduled["source"] == from_id:
                scheduled["source"] = to_id
            if scheduled["target"] == from_id:
                scheduled["target"] = to_id
        
        self.scheduled = [
            s for s in self.scheduled
            if s["source"] != s["target"]
        ]

        for cashback in self.cashbacks:
            if cashback["target"] == from_id:
                cashback["target"] = to_id

        for payment_id in self.payment_history:
            src = self.payment_history[payment_id]["source"]
            dst = self.payment_history[payment_id]["target"]

            if src == from_id:
                src = to_id
            if dst == from_id:
                dst = to_id

            if src != dst:
                self.payment_history[payment_id]["source"] = src
                self.payment_history[payment_id]["target"] = dst

        del self.accounts[from_id]

        return True

# -------------------------
# DRIVER CODE (so VS Code runs something)
# -------------------------

if __name__ == "__main__":

    bank = BankingSystem()

    print("\n===== TEST DRIVER START =====\n")

    # -------------------------
    print("1. Setup")
    print("Expected: create accounts → True True True")

    print(bank.create_account(1,"alice"))
    print(bank.create_account(2,"bob"))
    print(bank.create_account(3,"charlie"))

    bank.deposit(2,"alice",500)
    bank.deposit(3,"bob",300)

    print("Actual:", bank.accounts)
    print("Expected: alice=500, bob=300, charlie=0\n")


    # -------------------------
    print("2. Scheduled execution trigger")
    pid1 = bank.schedule_payment(4,"alice","bob",100,10)

    print("Before:", bank.accounts)

    bank.deposit(20,"alice",0)

    print("After:", bank.accounts)
    print("Expected: alice=400, bob=400\n")


    # -------------------------
    print("3. Ordering test (same execution time)")
    bank.deposit(21,"alice",500)

    p2 = bank.schedule_payment(22,"alice","bob",300,10)
    p3 = bank.schedule_payment(23,"alice","bob",300,9)

    bank.deposit(32,"alice",0)

    print("Actual:", bank.accounts)
    print("Expected: only ONE 300 should execute (ordering matters)\n")


    # -------------------------
    print("4. Insufficient balance")
    p4 = bank.schedule_payment(33,"alice","bob",10000,5)

    bank.deposit(40,"alice",0)

    print("Actual:", bank.accounts)
    print("Status:", bank.payment_status(40,p4))
    print("Expected: status = pending\n")


    # -------------------------
    print("5. Cashback")
    bank.deposit(50,"alice",500)

    p5 = bank.schedule_payment(51,"alice","bob",200,5)

    bank.deposit(57,"alice",0)          # execute
    bank.deposit(86400057,"alice",0)    # cashback

    print("Actual:", bank.accounts)
    print("Status:", bank.payment_status(86400057,p5))
    print("Expected: cashback added, status=completed\n")


    # -------------------------
    print("6. Cashback only once")

    before = bank.accounts["alice"]["balance"]
    bank.deposit(86400058,"alice",0)
    after = bank.accounts["alice"]["balance"]

    print("Actual:", before == after)
    print("Expected: True\n")


    # -------------------------
    print("7. Multiple cashback")

    bank.deposit(100,"alice",500)

    bank.schedule_payment(101,"alice","bob",100,5)
    bank.schedule_payment(102,"alice","bob",200,5)

    bank.deposit(107,"alice",0)
    bank.deposit(86400107,"alice",0)

    print("Actual:", bank.accounts)
    print("Expected: cashback = 2 + 4\n")


    # -------------------------
    print("8. Merge accounts")

    bank.deposit(200,"alice",300)
    bank.deposit(201,"charlie",200)

    print("Before merge:", bank.accounts)

    bank.merge_accounts(203,"alice","charlie")

    print("After merge:", bank.accounts)
    print("Expected: alice removed, values merged into charlie\n")


    # -------------------------
    print("9. Scheduled after merge")

    bank.schedule_payment(204,"charlie","bob",100,5)
    bank.deposit(210,"charlie",0)

    print("Actual:", bank.accounts)
    print("Expected: charlie → bob transfer works\n")


    # -------------------------
    print("10. Cashback after merge")

    p6 = bank.schedule_payment(211,"charlie","bob",200,5)

    bank.deposit(217,"charlie",0)

    bank.merge_accounts(220,"charlie","bob")

    bank.deposit(86400217,"bob",0)

    print("Actual:", bank.accounts)
    print("Expected: cashback goes to bob\n")


    # -------------------------
    print("11. Top spenders")

    print("Actual:", bank.top_spenders(999999,5))
    print("Expected: sorted by outgoing desc\n")


    # -------------------------
    print("12. Edge cases")

    print("Self transfer:", bank.transfer(300,"bob","bob",100))
    print("Expected: None")

    print("Unknown payment:", bank.payment_status(300,"payment999"))
    print("Expected: none\n")


    # -------------------------
    print("===== FINAL STATE =====")
    print("Accounts:", bank.accounts)
    print("Payments:", bank.payment_history)
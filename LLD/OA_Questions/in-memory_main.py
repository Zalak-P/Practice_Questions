class InMemoryDB:
    def __init__(self):
        self.hashmap = {}
        self.backups = []

    def set(self, key: str, field: str, value: str) -> str:
        if key not in self.hashmap:
            self.hashmap[key] = {}

        self.hashmap[key][field] = {
            "value": value,
            "expire": None
        }
        return ""

    def get(self, key: str, field: str) -> str:
        if key in self.hashmap and field in self.hashmap[key]:
            return self.hashmap[key][field]["value"]
        return ""

    def delete(self, key: str, field: str) -> str:
        if key not in self.hashmap or field not in self.hashmap[key]:
            return "false"

        del self.hashmap[key][field]

        if not self.hashmap[key]:
            del self.hashmap[key]

        return "true"
    
    def scan(self, key: str) -> str:
        if key not in self.hashmap:
            return ""

        result = []
        for field in sorted(self.hashmap[key]):
            result.append(f"{field}({self.hashmap[key][field]['value']})")

        return ", ".join(result)

    def scan_by_prefix(self, key: str, prefix: str) -> str:
        if key not in self.hashmap:
            return ""

        result = []
        for field in sorted(self.hashmap[key]):
            if field.startswith(prefix):
                result.append(f"{field}({self.hashmap[key][field]['value']})")

        return ", ".join(result)

    def cleanup(self, timestamp):

        keys_to_delete = []

        for key in self.hashmap:
            fields_to_delete = []

            for field in self.hashmap[key]:
                expire = self.hashmap[key][field]["expire"]

                if expire is not None and timestamp >= expire:
                    fields_to_delete.append(field)

            for field in fields_to_delete:
                del self.hashmap[key][field]

            if not self.hashmap[key]:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del self.hashmap[key]

    def set_at(self, key, field, value, timestamp):
        timestamp = int(timestamp)
        self.cleanup(timestamp)
        return self.set(key, field, value)

    def set_at_with_ttl(self, key, field, value, timestamp, ttl):
        timestamp = int(timestamp)
        ttl = int(ttl)

        self.cleanup(timestamp)

        if key not in self.hashmap:
            self.hashmap[key] = {}

        self.hashmap[key][field] = {
            "value": value,
            "expire": timestamp + ttl
        }
        return ""

    def get_at(self, key, field, timestamp):
        timestamp = int(timestamp)
        self.cleanup(timestamp)
        return self.get(key,field)

    def delete_at(self, key, field, timestamp):
        timestamp = int(timestamp)
        self.cleanup(timestamp)
        return self.delete(key, field)

    def scan_at(self, key, timestamp):
        timestamp = int(timestamp)
        self.cleanup(timestamp)
        return self.scan(key)

    def scan_by_prefix_at(self, key, prefix, timestamp):
        timestamp = int(timestamp)
        self.cleanup(timestamp)
        return self.scan_by_prefix(key,prefix)

    def backup(self, timestamp):

        timestamp = int(timestamp)
        self.cleanup(timestamp)

        snapshot = {}

        for key in self.hashmap:
            snapshot[key] = {}

            for field in self.hashmap[key]:
                value = self.hashmap[key][field]["value"]
                expire = self.hashmap[key][field]["expire"]

                remaining_ttl = None if expire is None else expire - timestamp

                snapshot[key][field] = (value, remaining_ttl)

        self.backups.append((timestamp, snapshot))

        return str(len(snapshot))
    
    def restore(self, timestamp, timestamp_to_restore):

        timestamp = int(timestamp)
        timestamp_to_restore = int(timestamp_to_restore)

        chosen_snapshot = None

        for backup_time, snapshot in self.backups:
            if backup_time <= timestamp_to_restore:
                chosen_snapshot = snapshot
            else:
                break

        self.hashmap = {}

        for key in chosen_snapshot:
            self.hashmap[key] = {}

            for field in chosen_snapshot[key]:
                value, remaining_ttl = chosen_snapshot[key][field]

                expire = None if remaining_ttl is None else timestamp + remaining_ttl

                self.hashmap[key][field] = {
                    "value": value,
                    "expire": expire
                }

        return ""

# ---------- UNIVERSAL DRIVER ----------
def run_test(queries):

    db = InMemoryDB()
    result = []

    for query in queries:
        op = query[0]

        if op == "SET":
            result.append(db.set(query[1], query[2], query[3]))

        elif op == "GET":
            result.append(db.get(query[1], query[2]))

        elif op == "DELETE":
            result.append(db.delete(query[1], query[2]))

        elif op == "SCAN":
            result.append(db.scan(query[1]))

        elif op == "SCAN_BY_PREFIX":
            result.append(db.scan_by_prefix(query[1], query[2]))

        elif op == "SET_AT":
            result.append(db.set_at(query[1], query[2], query[3], query[4]))

        elif op == "SET_AT_WITH_TTL":
            result.append(db.set_at_with_ttl(query[1], query[2], query[3], query[4], query[5]))

        elif op == "GET_AT":
            result.append(db.get_at(query[1], query[2], query[3]))

        elif op == "DELETE_AT":
            result.append(db.delete_at(query[1], query[2], query[3]))

        elif op == "SCAN_AT":
            result.append(db.scan_at(query[1], query[2]))

        elif op == "SCAN_BY_PREFIX_AT":
            result.append(db.scan_by_prefix_at(query[1], query[2], query[3]))

        elif op == "BACKUP":
            result.append(db.backup(query[1]))

        elif op == "RESTORE":
            result.append(db.restore(query[1], query[2]))

    return result


# ---------- TEST CASES ----------

print("LEVEL 1")
print(run_test([
["SET","A","B","E"],
["SET","A","C","F"],
["GET","A","B"],
["GET","A","D"],
["DELETE","A","B"],
["DELETE","A","D"]
]))

print("\nLEVEL 2")
print(run_test([
["SET","A","BC","E"],
["SET","A","BD","F"],
["SET","A","C","G"],
["SCAN_BY_PREFIX","A","B"],
["SCAN","A"],
["SCAN_BY_PREFIX","B","B"]
]))

print("\nLEVEL 3")
print(run_test([
["SET_AT_WITH_TTL","A","BC","E","1","9"],
["SET_AT_WITH_TTL","A","BC","E","5","10"],
["SET_AT","A","BD","F","5"],
["SCAN_BY_PREFIX_AT","A","B","14"],
["SCAN_BY_PREFIX_AT","A","B","15"]
]))

print("\nLEVEL 4")
print(run_test([
["SET_AT_WITH_TTL","A","B","C","1","10"],
["BACKUP","3"],
["SET_AT","A","D","E","4"],
["BACKUP","5"],
["DELETE_AT","A","B","8"],
["BACKUP","9"],
["RESTORE","10","7"],
["BACKUP","11"],
["SCAN_AT","A","15"],
["SCAN_AT","A","16"]
]))
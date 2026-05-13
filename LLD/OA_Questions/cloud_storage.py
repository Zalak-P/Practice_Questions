import copy
class CloudStorage:

    def __init__(self):
        self.files = {}
        self.users = {}
        self.backup = None

    def add_file(self, name: str, size: int) -> str:
        if "admin" not in self.users:
            self.users["admin"] = {"capacity": float("inf"), "used": 0}
        return self.add_file_by_user("admin", name, size)

    def get_file_size(self, name: str) -> str:
        if name not in self.files:
            return ""
        return str(self.files[name]["size"])

    def delete_file(self, name: str) -> str:
        if name not in self.files:
            return ""
        
        size = self.files[name]["size"]
        owner = self.files[name]["owner"]

        self.users[owner]["used"] -= size
        del self.files[name]
        return str(size)

    def get_n_largest(self, prefix: str, n: int) -> str:
        matched = []

        for name in self.files:
            if name.startswith(prefix):
                matched.append((name, self.files[name]["size"]))

        if not matched or n == 0:
            return ""

        matched.sort(key=lambda x: (-x[1], x[0]))

        result = []
        for name, size in matched[:n]:
            result.append(f"{name}({size})")

        return ", ".join(result)

    def add_user(self, user_id: str, capacity: int) -> str:
        if user_id in self.users:
            return "false"
        
        self.users[user_id] = {
            "capacity": capacity,
            "used": 0
        }
        return "true"
    
    def add_file_by_user(self, user_id: str, name: str, size: int) -> str:
        if name in self.files:
            return "false"

        if user_id not in self.users:
            return "false"

        if self.users[user_id]["used"] + size > self.users[user_id]["capacity"]:
            return "false"

        self.files[name] = {
            "size": size,
            "owner": user_id
        }

        self.users[user_id]["used"] += size
        return "true"
    
    def merge_user(self, user1: str, user2: str) -> str:
        if user1 not in self.users or user2 not in self.users:
            return "false"
        
        if user1 == user2:
            return "false"

        for name in self.files:
            if self.files[name]["owner"] == user2:
                self.files[name]["owner"] = user1

        self.users[user1]["used"] += self.users[user2]["used"]

        del self.users[user2]

        return "true"
    
    def backup_system(self) -> str:
        self.backup = {
            "files": copy.deepcopy(self.files),
            "users": copy.deepcopy(self.users)
        }
        return "true"
    
    def restore_system(self) -> str:
        if not self.backup:
            return "false"

        self.files = copy.deepcopy(self.backup["files"])
        self.users = copy.deepcopy(self.backup["users"])

        return "true"
    
def run_tests():
    cs = CloudStorage()

    print("----- LEVEL 1 -----")

    print(cs.add_file("/file1.txt", 10))   # true
    print(cs.add_file("/file1.txt", 20))   # false
    print(cs.get_file_size("/file1.txt"))  # 10
    print(cs.delete_file("/file1.txt"))    # 10
    print(cs.get_file_size("/file1.txt"))  # ""

    print("\n----- LEVEL 2 -----")

    cs.add_file("/dir/a.txt", 10)
    cs.add_file("/dir/b.txt", 20)
    cs.add_file("/dir/c.txt", 20)
    cs.add_file("/dir/sub/d.txt", 5)

    print(cs.get_n_largest("/dir", 2))
    # Expected: "/dir/b.txt(20), /dir/c.txt(20)"

    print(cs.get_n_largest("/dir", 10))
    # Expected: "/dir/b.txt(20), /dir/c.txt(20), /dir/a.txt(10), /dir/sub/d.txt(5)"

    print("\n----- LEVEL 3 -----")

    cs = CloudStorage()  # fresh system

    print(cs.add_user("A", 50))  # true
    print(cs.add_user("B", 100)) # true

    print(cs.add_file_by_user("A", "/a1.txt", 20))  # true
    print(cs.add_file_by_user("A", "/a2.txt", 40))  # false (capacity exceeded)

    print(cs.add_file_by_user("B", "/b1.txt", 30))  # true

    print(cs.get_file_size("/a1.txt"))  # 20

    print(cs.delete_file("/a1.txt"))    # 20

    print(cs.add_file_by_user("A", "/a3.txt", 30))  # true (space freed)

    print("\n----- LEVEL 4 (MERGE) -----")

    print(cs.add_file_by_user("B", "/b2.txt", 20))  # true

    print(cs.merge_user("A", "B"))  # true

    # After merge, B is gone, files belong to A
    print(cs.get_n_largest("/", 5))
    # Expected: all files under A

    print("\n----- LEVEL 4 (BACKUP/RESTORE) -----")

    print(cs.backup_system())  # true

    print(cs.delete_file("/b1.txt"))  # delete something

    print(cs.get_n_largest("/", 5))
    # Missing /b1.txt

    print(cs.restore_system())  # true

    print(cs.get_n_largest("/", 5))
    # /b1.txt should be back

    print("\n----- EDGE CASES -----")

    print(cs.add_user("A", 100))  # false (already exists)
    print(cs.merge_user("A", "A"))  # false
    print(cs.restore_system())  # true (backup exists)
    print(cs.get_n_largest("/unknown", 3))  # ""


# Run everything
run_tests()
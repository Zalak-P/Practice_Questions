import json
class TaskSystem:
    def __init__(self):
        self.users = {}
        self.tasks = {}
        self.assignment = {}
        self.task_id_counter = 1

    def add_task(self, timestamp: int, name: str, priority: int):
        task_id = "task_id_" + str(self.task_id_counter)
        self.task_id_counter += 1

        self.tasks[task_id] = {
            "name": name,
            "priority": priority,
            "timestamp": timestamp
        }
        return task_id
    
    def update_task(self, timestamp: int, task_id: str, name: str, priority: int):
        if task_id in self.tasks:
            self.tasks[task_id]["name"] = name
            self.tasks[task_id]["priority"] = priority
            return True
        return False
    
    def get_task(self, timestamp: int, task_id: str):
        if task_id not in self.tasks:
            return None
        
        return json.dumps({
            "name": self.tasks[task_id]["name"],
            "priority": self.tasks[task_id]["priority"]
        })

    def search_tasks(self, timestamp: int, name_filter: str, max_results: int):
        if max_results <= 0:
            return []

        task_order = []
        result = []
        for task_id in self.tasks:
            if name_filter in self.tasks[task_id]["name"]:
                task_order.append([task_id, self.tasks[task_id]["priority"]])

        task_order = sorted(task_order, key= lambda x: (-x[1], x[0]))

        for i in range(min(max_results, len(task_order))):
            result.append(task_order[i][0])
        return result

    def list_tasks_sorted(self, timestamp: int, limit: int):
        task_order = []
        result = []

        for task_id in self.tasks:
            task_order.append([task_id, self.tasks[task_id]["priority"]])

        task_order = sorted(task_order, key= lambda x: (-x[1], x[0]))

        for i in range(min(limit, len(task_order))):
            result.append(task_order[i][0])

        return result
    
    def add_user(self, timestamp: int, user_id: str, quota: int):
        if user_id not in self.users:
            self.users[user_id] = {
                "quota": quota
            }
            return True
        self.assignment[user_id] = []
        return False
    
    def assign_task(self, timestamp: int, task_id: str, user_id: str, finish_task: int):
        if task_id not in self.tasks or user_id not in self.users:
            return False
        active_tasks = 0
        for task in self.assignment[user_id]:
            if task["start"] <= timestamp < task["end"]:
                active_tasks += 1
        
        if active_tasks >= self.users[user_id]["quota"]:
            return False
        
        self.assignment[user_id].append({
            "start": timestamp,
            "end": finish_task,
            "task_id": task_id,
            "completed": False
        })

        return True
    
    def get_user_tasks(self, timestamp: int, user_id: str):
        if user_id not in self.users:
            return []

        result = []

        for task in self.assignment[user_id]:
            if task["start"] <= timestamp < task["end"]:
                result.append(task["task_id"])
        
        return result

# self.assignment = {
#     "alice": [
#         {"task_id": "task_id_1", "start": 2, "end": 10},
#         {"task_id": "task_id_2", "start": 5, "end": 8}
#     ]
# }
# -------------------------
# DRIVER CODE (so VS Code runs something)
# -------------------------

if __name__ == "__main__":
    system = TaskSystem()

    t1 = system.add_task(1,"build api",5)
    t2 = system.add_task(2,"write tests",3)
    t3 = system.add_task(3,"deploy",4)

    print(system.add_user(4,"alice",2))
    # True

    print(system.add_user(5,"alice",3))
    # False (already exists)

    print(system.assign_task(6,t1,"alice",10))
    # True

    print(system.assign_task(6,t2,"alice",9))
    # True

    print(system.assign_task(6,t3,"alice",12))
    # False (quota reached)

    print(system.get_user_tasks(7,"alice"))
    # ['task_id_1','task_id_2']

    print(system.get_user_tasks(9,"alice"))
    # ['task_id_1']

    print(system.assign_task(9,t3,"alice",15))
    # True

    print(system.get_user_tasks(10,"alice"))
    # ['task_id_1','task_id_3']
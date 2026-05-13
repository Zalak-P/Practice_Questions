from collections import deque

class InMemoryDBImpl:

    def __init__(self):
        self.db = {}
        self.modification_counts = {}

        self.locks = {}
        self.lock_queues = {}

    # ----------------------------
    # Internal helpers
    # ----------------------------

    def _set_or_inc_internal(self, key: str, field: str, value: int) -> int:

        if key not in self.db:
            self.db[key] = {}
            self.modification_counts[key] = 0

        if field in self.db[key]:
            self.db[key][field] += value
        else:
            self.db[key][field] = value

        self.modification_counts[key] += 1

        return self.db[key][field]

    def _delete_internal(self, key: str, field: str) -> bool:

        if key in self.db and field in self.db[key]:

            del self.db[key][field]
            self.modification_counts[key] += 1

            if not self.db[key]:

                del self.db[key]
                del self.modification_counts[key]

                # clean locks if record disappears
                if key in self.locks:
                    del self.locks[key]

                if key in self.lock_queues:
                    del self.lock_queues[key]

            return True

        return False

    # ----------------------------
    # Level 1 operations
    # ----------------------------

    def set_or_inc(self, key: str, field: str, value: int) -> int | None:

        if key in self.locks:
            return self.get(key, field)

        return self._set_or_inc_internal(key, field, value)

    def get(self, key: str, field: str) -> int | None:

        if key in self.db and field in self.db[key]:
            return self.db[key][field]

        return None

    def delete(self, key: str, field: str) -> bool:

        if key in self.locks:
            return False

        return self._delete_internal(key, field)

    # ----------------------------
    # Level 2
    # ----------------------------

    def top_n_keys(self, n: int) -> list[str]:

        sorted_keys = sorted(
            self.modification_counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        return [f"{k}({v})" for k, v in sorted_keys[:n]]

    # ----------------------------
    # Level 3 caller-based ops
    # ----------------------------

    def set_or_inc_by_caller(
        self, key: str, field: str, value: int, caller_id: str
    ) -> int | None:

        if key in self.locks and self.locks[key] != caller_id:
            return self.get(key, field)

        return self._set_or_inc_internal(key, field, value)

    def delete_by_caller(self, key: str, field: str, caller_id: str) -> bool:

        if key in self.locks and self.locks[key] != caller_id:
            return False

        return self._delete_internal(key, field)

    # ----------------------------
    # Level 4 locking
    # ----------------------------

    def lock(self, caller_id: str, key: str) -> str | None:

        if key not in self.db:
            return "invalid_request"

        if key not in self.locks:
            self.locks[key] = caller_id
            return "acquired"

        if self.locks[key] == caller_id:
            return None

        if key not in self.lock_queues:
            self.lock_queues[key] = deque()

        if caller_id not in self.lock_queues[key]:
            self.lock_queues[key].append(caller_id)

        return "wait"

    def unlock(self, key: str) -> str | None:

        if key not in self.db:
            return "invalid_request"

        if key not in self.locks:
            return None

        del self.locks[key]

        if key in self.lock_queues and self.lock_queues[key]:
            next_user = self.lock_queues[key].popleft()
            self.locks[key] = next_user

        if key in self.lock_queues and not self.lock_queues[key]:
            del self.lock_queues[key]

        return "released"
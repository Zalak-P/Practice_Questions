import threading
class ThreadSafeLockingSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        with cls._lock:
            if cls._instance is None:
                print("Singleton Constructor Called!")
                cls._instance = super().__new__(cls)

            return cls._instance

s1 = ThreadSafeLockingSingleton()
s2 = ThreadSafeLockingSingleton()

print(s1 is s2)


# Core Idea:
# Every time object creation is attempted:
# ThreadSafeLockingSingleton()
# the method acquires a lock.
# Only one thread can enter at a time.
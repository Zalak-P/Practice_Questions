import threading

class ThreadSafeDoubleLockingSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("Creating Singleton Object...")
                    cls._instance = super().__new__(cls)

        return cls._instance

s1 = ThreadSafeDoubleLockingSingleton()
s2 = ThreadSafeDoubleLockingSingleton()

print(s1 is s2)
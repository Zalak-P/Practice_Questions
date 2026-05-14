import threading

class ThreadSafeDoubleLockingSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # First check: no lock
        if cls._instance is None:

            # Lock only if object is not created yet
            with cls._lock:
            # ACQUIRE LOCK, Only ONE thread can enter here at a time.

                # Second check: after getting lock-> WHY: Another thread may have already created object while current thread was waiting for lock.
                if cls._instance is None:
                    print("Creating Singleton Object...")
                    cls._instance = super().__new__(cls)

        return cls._instance

s1 = ThreadSafeDoubleLockingSingleton()
s2 = ThreadSafeDoubleLockingSingleton()

print(s1 is s2)
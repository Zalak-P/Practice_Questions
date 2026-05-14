import threading

class ThreadSafeDoubleLockingSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # -----------------------------------------
        # First Check
        # No locking yet.
        # Avoids unnecessary locking after Singleton already exists.
        # -----------------------------------------

        if cls._instance is None:
            # -----------------------------------------
            # Acquire Lock
            # Only ONE thread can enter here.
            # -----------------------------------------

            with cls._lock:
                # -----------------------------------------
                # Second Check
                # Another thread may have already
                # created object while current thread
                # was waiting for lock.
                # -----------------------------------------
                if cls._instance is None:
                    print("Creating Singleton Object...")
                    cls._instance = super().__new__(cls)

        return cls._instance

s1 = ThreadSafeDoubleLockingSingleton()
s2 = ThreadSafeDoubleLockingSingleton()

print(s1 is s2)
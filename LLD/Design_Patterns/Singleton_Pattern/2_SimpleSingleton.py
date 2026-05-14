class Singleton:
    
    _instance = None    # CLASS variable -> this belongs to Class, not object, only 1 shared copy

    # -----------------------------------------------------
    # __new__(): Responsible for ACTUALLY CREATING the object.
    # This runs BEFORE __init__().
    # Since Singleton needs to CONTROL object creation, Singleton logic is written inside __new__().
    # -----------------------------------------------------
    def __new__(cls):  # Create object only ONCE
        if cls._instance is None:
            print("Creating Singleton Object...")
            cls._instance = super().__new__(cls)  # allocates memory, creates object and store the object reference
        # Return SAME object every time
        return cls._instance

    # -----------------------------------------------------
    # __init__()
    # Responsible for INITIALIZING object AFTER creation.
    # Important: __init__ does NOT create object. Since object already exists during second call, __init__ may still run again.
    # -----------------------------------------------------
    def __init__(self):
        print("Init called")

print("----- Singleton Example -----")
obj1 = Singleton()
obj2 = Singleton()
print("obj1 == obj2 :", obj1 == obj2)
print("obj1 is obj2 :", obj1 is obj2) # Same object: Output -> True

# =========================================================
# MEMORY ADDRESS CHECK
# =========================================================

print("----- Memory Address Check -----")
print("obj1 id:", id(obj1))
print("obj2 id:", id(obj2)) # Same memory address

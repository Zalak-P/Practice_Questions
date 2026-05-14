class NoSingleton:

    def __init__(self):
        print("New Object created.")


print("----- No Singleton Example -----")
s1 = NoSingleton()
s2 = NoSingleton()
print("s1", s1)
print("s2", s2)
print("s1 is s2 :", s1 is s2)

# Output:
# False

# 1. __init__()
# Runs after object creation.
# Used for object initialization.

# 2. s1 = NoSingleton()
# Python internally calls:
# - __new__() -> creates object
# - __init__() -> initializes object

# 3. s2 = NoSingleton()
# Another completely new object gets created.

# 4. s1 is s2
# 'is' checks whether both variables point to the SAME object.

# because:
# - s1 points to Object A
# - s2 points to Object B
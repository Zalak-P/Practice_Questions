class NoSingleton:
    def __init__(self):
    # Runs AFTER object is created.
    # Purpose: initialize object. NOT create object. Very important.
    print("New Object created.")

print("----- No Singleton Example -----")

# s1 -> Object Creation, Python internally does __new__() creates object in memory.
s1 = NoSingleton()
# SAME happens again. Another brand NEW object created.
s2 = NoSingleton()

print("s1", s1)
print("s2", s2) # this will return two different objects
print("s1 is s2 :", s1 is s2) # is checks Memory identity: Output -> False
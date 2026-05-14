class ThreadSafeEagerSingleton:
    def __init__(self):
        print("Singleton Constructor Called!")

# ---------------------------------------------------
# EAGER OBJECT CREATION: Object created IMMEDIATELY.
# Unlike Lazy Singleton: Object is NOT waiting until first request.
# ---------------------------------------------------
instance = ThreadSafeEagerSingleton()

def get_instance():
    return instance

# ========================================================
# MAIN
# =========================================================

s1 = get_instance()
s2 = get_instance()
print(s1 is s2)

# Output:
# Singleton Constructor Called!
# True


# =========================================================
# IMPORTANT DIFFERENCE:
# JAVA vs PYTHON
# =========================================================
'''
# ---------------------------------------------------
# JAVA SINGLETON
# ---------------------------------------------------
Java uses: private Constructor
private Singleton()
“Nobody outside this class can call the constructor.”

So THIS becomes illegal:
new ThreadSafeEagerSingleton();
outside the class.

Only the class itself can create object.
That is how Java STRICTLY enforces Singleton.
# ---------------------------------------------------
# PYTHON SINGLETON
# ---------------------------------------------------
Python does NOT have true private constructors.

Even if you write:
def __init__(self):

users can STILL do:
obj = MySingleton()
from outside.

Python does not block that.

class MyClass:
    pass
a = MyClass()
b = MyClass()
always allowed.

Python "Private" Is Mostly Convention.

Example:
_instance or __something
only means: “Please don't touch this.”

It is NOT true access restriction like Java.

Therefore Strict Singleton Is Harder in Python.
That is why Python Singleton implementations often use:
__new__()
metaclasses
module-level objects
to CONTROL creation behavior.

But Python still cannot enforce privacy the same way Java can.
'''
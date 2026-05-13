# ======================================================
# PRODUCT HIERARCHY
# ======================================================

# Base class for all burgers
# Every burger must implement prepare()

class Burger:
    def prepare(self):
        pass

# ---------------- REGULAR BURGERS ----------------

# Concrete product
class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")

# Concrete product
class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")

# Concrete product
class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

# ---------------- WHEAT BURGERS ----------------

# Concrete product
class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")

# Concrete product
class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing Standard Wheat Burger with bun, patty, cheese, and lettuce!")

# Concrete product
class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

# ======================================================
# FACTORY HIERARCHY
# ======================================================

# Base factory class
# Every factory must know how to create burgers

class BurgerFactory:
    def create_burger(self, burger_type):
        pass

# ======================================================
# CONCRETE FACTORIES
# ======================================================

# Singh factory creates REGULAR burgers

class SinghBurger(BurgerFactory):
    def create_burger(self, burger_type):

        # Factory decides which object to instantiate
        if burger_type.lower() == "basic":
            return BasicBurger()
        elif burger_type.lower() == "standard":
            return StandardBurger()
        elif burger_type.lower() == "premium":
            return PremiumBurger()
        else:
            print("Invalid burger type!")
            return None

# King factory creates WHEAT burgers
class KingBurger(BurgerFactory):
    def create_burger(self, burger_type):

        # Same method
        # But different object creation logic
        if burger_type.lower() == "basic":
            return BasicWheatBurger()
        elif burger_type.lower() == "standard":
            return StandardWheatBurger()
        elif burger_type.lower() == "premium":
            return PremiumWheatBurger()
        else:
            print("Invalid burger type!")
            return None

# ======================================================
# MAIN
# ======================================================

# Client asks for burger type
burger_type = "basic"

# Polymorphism:
# BurgerFactory reference can point to any factory
my_factory = SinghBurger()

# Runtime:
# SinghBurger.create_burger("basic") gets called
burger = my_factory.create_burger(burger_type)

# burger now contains:
# BasicBurger object
if burger:
    # Runtime polymorphism:
    # BasicBurger.prepare() gets executed
    burger.prepare()
# ======================================================
# PRODUCT FAMILY 1 --> BURGER
# ======================================================

class Burger:
    def prepare(self):
        pass

# ---------------- REGULAR BURGERS ----------------
class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")

class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")

class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

# ---------------- WHEAT BURGERS ----------------

class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")

class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing Standard Wheat Burger with bun, patty, cheese, and lettuce!")

class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

# ======================================================
# PRODUCT FAMILY 2 --> GARLIC BREAD
# ======================================================

class GarlicBread:
    def prepare(self):
        pass

# ---------------- REGULAR GARLIC BREAD ----------------

class BasicGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Basic Garlic Bread with butter and garlic!")

class CheeseGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Cheese Garlic Bread with extra cheese and butter!")

# ---------------- WHEAT GARLIC BREAD ----------------

class BasicWheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Basic Wheat Garlic Bread with butter and garlic!")

class CheeseWheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Cheese Wheat Garlic Bread with extra cheese and butter!")

# ======================================================
# ABSTRACT FACTORY
# ======================================================

class MealFactory:
    def create_burger(self, burger_type):
        pass

    def create_garlic_bread(self, bread_type):
        pass

# ======================================================
# CONCRETE FACTORY 1
# ======================================================

class SinghBurger(MealFactory):

    # Creates regular burgers
    def create_burger(self, burger_type):

        if burger_type.lower() == "basic":
            return BasicBurger()

        elif burger_type.lower() == "standard":
            return StandardBurger()

        elif burger_type.lower() == "premium":
            return PremiumBurger()

        else:
            print("Invalid burger type!")
            return None

    # Creates regular garlic breads
    def create_garlic_bread(self, bread_type):

        if bread_type.lower() == "basic":
            return BasicGarlicBread()

        elif bread_type.lower() == "cheese":
            return CheeseGarlicBread()

        else:
            print("Invalid garlic bread type!")
            return None

# ======================================================
# CONCRETE FACTORY 2
# ======================================================

class KingBurger(MealFactory):

    # Creates wheat burgers
    def create_burger(self, burger_type):

        if burger_type.lower() == "basic":
            return BasicWheatBurger()

        elif burger_type.lower() == "standard":
            return StandardWheatBurger()

        elif burger_type.lower() == "premium":
            return PremiumWheatBurger()

        else:
            print("Invalid burger type!")
            return None

    # Creates wheat garlic breads
    def create_garlic_bread(self, bread_type):

        if bread_type.lower() == "basic":
            return BasicWheatGarlicBread()

        elif bread_type.lower() == "cheese":
            return CheeseWheatGarlicBread()

        else:
            print("Invalid garlic bread type!")
            return None

# ======================================================
# MAIN
# ======================================================

burger_type = "basic"
garlic_bread_type = "cheese"

# MealFactory reference can point to any factory
meal_factory = SinghBurger()

# Factory creates related product family
burger = meal_factory.create_burger(burger_type)
garlic_bread = meal_factory.create_garlic_bread(garlic_bread_type)

# Runtime polymorphism
if burger:
    burger.prepare()

if garlic_bread:
    garlic_bread.prepare()
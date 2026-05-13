# Video Soln: https://www.youtube.com/watch?v=dMK4TbG29fk

# --- Burger Base Class ---
class Burger:
    def prepare(self):
        pass


# --- Concrete Burger Implementations ---
class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")


class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")


class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")


# --- Burger Factory ---
class BurgerFactory:

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


# --- Main ---
burger_type = "standard"

factory = BurgerFactory()

burger = factory.create_burger(burger_type)

if burger:
    burger.prepare()
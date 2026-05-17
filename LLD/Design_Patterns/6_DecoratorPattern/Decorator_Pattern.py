from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_abilities(self):
        pass

class Mario(Character):
    def get_abilities(self):
        return "Mario"

class CharacterDecorator(Character):
    def __init__(self, character):
        self.character = character

class HeightUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " with HeightUp"

class GunPowerUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " with Gun"

class StarPowerUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " with Star Power (Limited Time)"

mario = Mario()
print("Basic Character:", mario.get_abilities())

mario = HeightUp(mario)
print("After HeightUp:", mario.get_abilities())

mario = GunPowerUp(mario)
print("After GunPowerUp:", mario.get_abilities())

mario = StarPowerUp(mario)
print("After StarPowerUp:", mario.get_abilities())

# Output:
# Basic Character: Mario
# After HeightUp: Mario with HeightUp
# After GunPowerUp: Mario with HeightUp with Gun
# After StarPowerUp: Mario with HeightUp with Gun with Star Power (Limited Time)
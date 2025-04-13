# Base Class
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.__secret_identity = "Unknown"  # Encapsulated attribute

    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__secret_identity}."

    def set_identity(self, identity):
        self.__secret_identity = identity

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass 1
class SpeedHero(Superhero):
    def use_power(self):
        print(f"{self.name} has the speed of lightning {self.power}! ")

# Subclass 2
class StrengthHero(Superhero):
    def use_power(self):
        print(f"{self.name} smashes with {self.power}!")

# Create heroes
the_flash = SpeedHero("The Flash", "Super Speed")
the_flash.set_identity("Barry Allen")

Hulk = StrengthHero("Hulk", "Super Strength")
Hulk.set_identity("Bruce Banner")

# Test them
the_flash.use_power()
print(the_flash.reveal_identity())

Hulk.use_power()
print(Hulk.reveal_identity())

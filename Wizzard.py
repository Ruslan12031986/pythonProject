from Unit import Unit
from random import choice
from enum import Enum

class Wizzard(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intelligence=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intelligence = intelligence

        super().__init__(name, health, power, agility, intelligence)

    def get_level_up(self):
        self.intelligence +=1
        if self.intelligence >= 10:
            self.intelligence = 1
        return self.intelligence

    def __str__(self):
        return f"Name: {self.name}\nhealth {self.health}\npower {self.power}\nagility {self.agility}"

class WizzardSkills(Enum):
    WIND = "wind"
    FIRE = "fire"
    WATER = "water"
    @classmethod
    def get_skill(cls):
        return choice([WizzardSkills.WIND, WizzardSkills.FIRE, WizzardSkills.WATER])


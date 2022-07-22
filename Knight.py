from Unit import Unit
from random import choice
from enum import Enum

class Knight(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intelligence=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intelligence = intelligence

        super().__init__(name, health=100, power=1, agility=1, intelligence=1)

    def get_level_up(self):
        self.power +=1
        if self.power >= 10:
            self.power = 1
        return self.power

    def __str__(self):
        return f"Name: {self.name}\nhealth {self.health}\npower {self.power}\nagility {self.agility}"

class KnightSkills(Enum):
    SWORD = "sword"
    AXE = "axe"
    PIKE = "pike"
    @classmethod
    def get_skill(cls):
        return choice([KnightSkills.SWORD, KnightSkills.AXE, KnightSkills.PIKE])
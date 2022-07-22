from Unit import Unit
from random import choice
from enum import Enum

class Archer(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intelligence=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intelligence = intelligence

        super().__init__(name, health=100, power=1, agility=1, intelligence=1)

    def get_level_up(self):
        self.agility +=1
        if self.agility >= 10:
            self.agility = 1
        return self.agility

    def __str__(self):
        return f"Name: {self.name}\nhealth {self.health}\npower {self.power}\nagility {self.agility}"

class ArcherSkills(Enum):
    BOW = "bow"
    CROSSBOW = "crossbow"
    SLING = "sling"
    @classmethod
    def get_skill(cls):
        return choice([ArcherSkills.BOW, ArcherSkills.CROSSBOW, ArcherSkills.SLING])
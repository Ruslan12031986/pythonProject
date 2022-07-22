from random import randint

from abc import ABCMeta, abstractmethod


class Unit(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, health=100, power=1, agility=1, intelligence=1):
        if 0 < health <= 100 and 0 < power <= 10 and 0 < agility <= 10 and 0 < intelligence <= 10:
            self.name = name
            self.health = health
            self.power = power
            self.agility = agility
            self.intelligence = intelligence
        else:
            raise TypeError("invalid data")

    def health_up (self):
        randomNumber = randint(1, 20)
        self.health += randomNumber/100
        if self.health > 100:
            self.health = 100
        return self.health

    def health_down (self):
        if self.health >=1:
            randomNumber = randint(1, 20)
            self.health -= randomNumber/100
            if self.health <1:
                self.health = 0
        return self.health

    @abstractmethod
    def get_level_up (self):
        pass

    def __str__(self):
        return f"Name: {self.name}\nhealth {self.health}\npower {self.power}\nagility\n {self.agility}"

from Wizzard import Wizzard, WizzardSkills
from Archer import Archer, ArcherSkills
from Knight import Knight, KnightSkills

wizzard = Wizzard(name="Gendalf")
archer = Archer(name="Legolas")
knight = Knight(name="Mike")

level_wizzard = wizzard.get_level_up()
health_up = wizzard.health_up()
health_down = wizzard.health_down()

print(health_up)
print(health_down)

skill1=WizzardSkills.get_skill()

level_archer = archer.get_level_up()
archer.health_up()
archer.health_down()

skill2=ArcherSkills.get_skill()

level_knight = knight.get_level_up()
knight.health_up()
knight.health_down()

skill3=KnightSkills.get_skill()

print(level_wizzard)
print(level_archer)
print(level_knight)

print(skill1)
print(skill2)
print(skill3)

print(wizzard)
print(archer)
print(knight)
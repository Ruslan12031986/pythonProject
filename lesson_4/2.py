# Є слот машина на барабані якої 5 картинок, серед яких є Джокер.
#    Наприклад ['cherry', 'lemon', 'watermelon', '7', 'JOKER'].
#    Треба зробити так , щоб джокер випадав приблизно в два рази рідше ніж всі решта.

import random

lucky_list = ['cherry', 'lemon', 'watermelon', '7', 'JOKER']
lucky_list_2 = ['cherry', 'lemon', 'watermelon', '7']
s = None
while s != 'N':
    s = input('Играем дальше:')
    a = random.random()
    if a < 0.1:
        print('Joker')
    else:

        print(random.choice(lucky_list_2))


#Створити список із n випадкових цілих чисел з діапазону (1, М).
#   n та М отримати з клавіатури запитом користувача (input).


from random import randint
a = int(input("Введите число: "))
l = [(randint(1, a)) for i in range(a)]
print(l)

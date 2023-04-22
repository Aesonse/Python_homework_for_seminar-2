"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть. 
Стороны монеты вводятся построчно или в одну строку, если умеете."""

n = int(input("Введите количество монет: "))
count_r = 0
count_g = 0
for i in range(n):
    coin = input(f"Введите сторону {i+1} монеты (r - решка, g - герб): ")
    if coin == "r":
        count_r += 1
    if coin == "g":
        count_g += 1
print("Mинимальное количество монет, которые нужно перевернуть: ")
if count_r < count_g:
    print(count_r)
else: print(count_g)
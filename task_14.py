"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N."""
n = int(input("Введите число: "))
number = 2
result = number
print(f"Степени числа {number} до указанного числа: ")
while n >= result*2:
	print(result, end = ', ')
	result *= number
print(result)
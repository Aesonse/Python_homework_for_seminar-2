"""Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
 Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P.Помогите Кате отгадать задуманные Петей числа."""
s = int(input("Введите сумму Х и Y: "))
p = int(input("Введите произведение X и Y: "))
solution  = False
for x in range(s//2+1):
	y = s - x
	if x*y==p:
		solution = True
		print(f"X={x}, Y={y}")
if not solution:
	print("нет решений")
import random

lenght = int(input("LEN: "))
mini = int(input('MIN: '))
maxi = int(input("MAX: "))

array = []

for i in range(0,lenght):
	array.append(random.randint(0,100))

for num in array:
	if num <=maxi and num >= mini:
		print("Число "+str(num)+" находиться в диапазоне")
	else:
		print("Число "+str(num)+" НЕ находиться в диапазоне")
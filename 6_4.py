import random

array = []

for i in range(1,10):
	array.append(random.randint(0,9))

for num in array:
	if num >= 0 and num <=3:
		print("1>>3"+" "+str(num))
	if num >= 4 and num <=6:
		print("4>>6"+" "+str(num))
	if num >= 7 and num <=9:
		print("7>>9"+" "+str(num))

import random

array = []
for array_num in range(10):
	array.append(random.randint(1,50))
yes = no = 0
for num in array:
	if num % 2 == 0:
		yes += 1
	else:
		no += 1

print("Сгенерированные случайные числа массива: "+str(array)+"\nЧётных: "+str(yes)+"\nНечётных: "+str(no))
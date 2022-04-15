import random

array = [] 
array_hi = []
array_lo = []
for array_num in range(10):
	array.append(random.randint(-50,50))
yes = no = 0
for num in array:
	if num >= 0:
		array_hi.append(str(num))
	else:
		array_lo.append(str(num))

print("Сгенерированные случайные числа массива: "+str(array)+"\nПоложительные: "+" ".join(array_hi)+"\nОтрицательные: "+" ".join(array_lo))
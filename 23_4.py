import numpy as np

try:
	a = np.array(range(14), float)
	a = a.reshape((7,7))
except:
	print("Ошибка, нельзя создать массив 7*7 из 14 элементов")
	a = np.array(range(49), float)
	a = a.reshape((7,7))
print(a)
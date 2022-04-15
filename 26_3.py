import numpy as np
import random

def moveArrayto90(array):
	return [list(reversed(col)) for col in zip(*array)]

array = np.array(range(64))

array = array.reshape((8,8))

i = 0

print(array)

array = moveArrayto90(array) 

for __ in array:
	j = 0
	for ___ in __:
		array[i][j] = random.randint(0,100)
		j+=1
	array[i].sort()
	i+=1

array = moveArrayto90(array)

for __ in array:print(__)
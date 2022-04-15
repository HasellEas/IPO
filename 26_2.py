import numpy as np
import random

array = np.array(range(49))

array = array.reshape((7,7))

i = 0

for __ in array:
	j = 0
	for ___ in __:
		array[i][j] = random.randint(0,100)
		j+=1
	array[i].sort()
	i+=1
	
print(array)
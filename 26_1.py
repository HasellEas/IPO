import numpy as np
import random

array = np.array(range(20))

for __ in array:
	array[__] = random.randint(0,100)

array.sort()

print(array)
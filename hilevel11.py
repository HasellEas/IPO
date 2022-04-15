import numpy as np
import random

array = np.array(range(16), int)
for __ in array: array[__] = random.randint(-20,20)

array = array.reshape((4,4))

print(array)

S=0
array = array.flatten()
for __ in array: 
	if 1<int(__) and int(__)<6:
		S+=1  
print(S)
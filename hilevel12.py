import numpy as np
import random

array = np.array(range(25), int)
for __ in array: array[__] = random.randint(-20,20)

array = array.reshape((5,5))

print(array)

print("Произведение min*max = "+str(array.min()*array.max()))

queue = {
(1,1), (1,3), (2,1), (2,4), (3,2), (3,5), (4,1), (4,3), (5,2), (5,5) }

S=0
for __ in queue:
	S+=array[__[0]-1,__[1]-1]

print("Сумма элементов: "+str(S))
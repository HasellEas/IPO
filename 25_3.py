import numpy
import random

b = numpy.array(range(10), int)
for __ in b:
	b[__] == random.randint(0,100)

a = numpy.array(range(10), int)
for __ in a:
	a[__] == 1 / random.randint(0,100)

aTrueSort = a != 2
bTrueSort = b != 2

newArray = []
for __ in range(0,int(len(a))):
	if aTrueSort[__] == True and bTrueSort[__] == True:
		newArray.append(a[__])

print(newArray)
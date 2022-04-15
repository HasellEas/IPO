# Дан одномерный массив из Н элементов
# подсчитать количество чисел делящихся на 3 нацело
# средне арифметическое с чётными значениями
# поставить полученые величины на первое и последнеее место в массиве

import numpy
import random

b = numpy.array(range(int(input("N: "))), int)

for __ in b:
	b[__] = random.randint(0,100)

count3del = 0
arrayChet = []

for __ in b:
	if __ % 3 == 0:
		count3del+=1
	if __ % 2 == 0:
		arrayChet.append(__)

print("Количество чисел делящихся нацело на 3: "+str(count3del))

print(numpy.array(arrayChet, int).sum())
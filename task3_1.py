a = input("int: ")
m = list(a)
b = 0
c = 1
for n in m:
	b += int(n)
	c *= int(n)
print("Сумма чисел: "+str(b)+"\nПроизведение чисел: "+str(c))
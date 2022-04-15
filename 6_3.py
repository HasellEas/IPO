array = []
for i in range(0,8):
	array.append(input())

print("Это имена несорт: "+" ".join(array))
array.sort()
print("Это имена сорт: "+" ".join(array)+"\n")

while True:
	text = ''
	i=0
	for num in array:
		i+=1
		text+= "#"+str(i)+" "+str(num)+'\n'
	editarray = int(input("Жалете изменить одно из имён?\n"+text+"Номер: "))
	name = input("Имя: ")
	array[editarray-1] = name
	print("Это имена сорт: "+" ".join(array))
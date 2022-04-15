array = []
for i in range(0,8):
	array.append(input())

print("Это имена несорт: "+" ".join(array))
array.sort()
print("Это имена сорт: "+" ".join(array))
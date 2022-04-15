array = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
i=0
for num in array:
	if num >= 0 and num != 0:
		array[i] = 1
	elif num == 0:
		None
	else:
		array[i] = 0
	i+=1

print(array)
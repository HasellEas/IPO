while True:
	try:
		num = int(input("input: "))
		break
	except:
		print("Некоректные данные, повторите ввод")

if num%4 == 0 and num!=0:
	print("Кратное 4ём")
else:
	print("Не кратное 4ём")
if num%2 == 0:
	print("Чётное")
else:
	print("Нечётное")
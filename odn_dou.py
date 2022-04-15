import sys
while True:
	try:
		num = input("input: ")
		check_is_int = int(num)
		break
	except:
		print("Некоректные данные, повторите ввод")
if len(num) == 1:
	print("Однозначное")
else:
	if len(num) >= 4 and int(num) < 0:
		print("Некоректный ввод")
		sys.exit()
	if len(num) >= 3 and int(num) > 0:
		print("Некоректный ввод")
		sys.exit()
	if int(num) < 0 and len(num) == 2:
		print("Однозначное") 
	else:
		print("Двухзначное")
if int(num) >=0: 
	print("Положительное") 
else: 
	print("Отрицательное")
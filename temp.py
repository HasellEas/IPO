while True:
	try:
		temp = int(input("input: "))
		break
	except:
		print("Некоректные данные, повторите ввод")

if temp > 10 and temp < 60 and temp > -20:
	print("Хорошо")
elif temp >= 60:
	print("Слишком жарко")
elif temp <= -25:
	print("Слишком холодно")
else:
	print("Прошладно")
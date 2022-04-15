from ast import literal_eval

def del_from_tuple(inpute, delete):
	text_output = "("
	for num in inpute:
		if num != delete:
			text_output+=str(num)+","
	return literal_eval(text_output[0:-1] + ")")

print(del_from_tuple(literal_eval(input("Кортеж: "), literal_eval(input("Удалить:"))	))
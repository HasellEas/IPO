def shortener(text):
	text_array = list(text)
	output_text = ""
	offoutput = 0
	for num in text_array:
		if num == "(":
			offoutput = 1
			continue
		if num == ")":
			offoutput = 0
			continue
		if offoutput == 0:
			output_text+=str(num)
	clear_ouput = output_text.split()
	return " ".join(clear_ouput)

print(shortener(input()))
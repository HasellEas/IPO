text = input()
text_array =list(text)
output = []
posit = 0

for word in text_array:
	if not word.isalpha():
		output.append(word.upper())
		continue
	if posit == 0:
		posit = 1
		output.append(word.upper())
	else:
		posit = 0
		output.append(word.lower())
print("\n"+"".join(output))
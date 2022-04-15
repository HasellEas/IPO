text = input("Text: ")
text_array_split = text.split()
array_for_output = []
for word in text_array_split:
	array_for_output.append(len(word))
print("Минимальная длина: "+str(min(array_for_output))+" \nСтрока: "+text_array_split[array_for_output.index(min(array_for_output))])
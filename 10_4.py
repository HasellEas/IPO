file = input("DIR: ")

with open(file, "r") as __:
    file_text = __.read()
file = open(file, "r")
c=0
for __ in file.readline():
	c += 1
print("Строк:"+str(c)+"\nСимволов: "+str(len(file_text))+"\nСлов: "+str(len(file_text.split())))
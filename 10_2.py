import re

file = input("DIR: ")
with open(file, "r") as __:
    text = __.read()
split = text.split()
for word in split:
    if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", word)):
        print(word)
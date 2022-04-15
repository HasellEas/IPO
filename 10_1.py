file = input("DIR: ")

with open(file, "r") as __:
    text = __.read()

split = text.split()

split.sort()

new = ''

for __ in split:
    new += str(__)+"\n"

with open("sort_plan.txt", "w") as __:
    __.write(new)
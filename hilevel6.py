def read_last(lines, file):
    with open(file,"r",encoding="utf-8") as __:
        fnc = []
        while True:
            a = __.readline()
            if not a:
                break
            fnc.append(a)
    return fnc[:lines]

print(read_last(4, "Вечерело.txt"))
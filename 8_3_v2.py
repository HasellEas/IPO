lists = [["G-22",["Дмитриев Дмитрий", "Азаров Назар", "Матвеев Матвей"]],["F-22",["Масимов Максим", "Алексеев Алексей", "Павлов Павел"]], ["S-22",["Иванов Иван", "Семёнов Семён", "Васильев Василий"]]]

for __ in lists:
    print(__[0])
    for ___ in __[1]:
        if ___.split()[0][0].lower() == "а": 
            print(___)
    print("\n")
from colorama import *
init(convert=True)

dates = ["Понедельник","Вторник","Среда","Чертверг","Пятница","Суббота","Воскресение"]

out = ''

i = 0

while True:
    for date in dates:
        if date == "Суббота" or date == "Воскресение":
            date = Fore.GREEN+date+Style.RESET_ALL+" B"
        else:
            date = Fore.RED+date+Style.RESET_ALL+" Р"
        out += date+" "+str(i+1)+" | "
        i+=1
        if i == 31:
            break
    out+='\n'
    if i == 31:
        break

print(out)
text = """
Понедельник
    Физика (лекц.)
    Физика (лаб.)
    Алгебра (практ.)
Вторник
    Геометрия (лекц.)
    Физика (практ.)
    Физика (лаб.)
    Физкультура (практ.)
Среда
    Физика (лекц.)
    Физика (практ.)
    Физкультура (практ.)
Четверг
    Физика (лаб.)
    Алгебра (практ.)
    Физика (лекц.)
Пятница
    Геометрия (лекц.)
    Физика (практ.)
    Физика (лаб.)
    Физкультура (практ.)
"""
with open("sps.txt","w",encoding="utf-8") as R:
    R.write(text)
nums = {}
ignore = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
file_read = open("sps.txt","r",encoding="utf-8")
while True:
    __ = str(file_read.readline())
    __ = __.replace("\t","")
    __ = __.replace("  ","")
    if not __:
        file_read.close()
        break
    if str(__) in nums:
        nums[str(__)]+=1
    else:
        nums.update({str(__):0})
        nums[str(__)]+=1
for __, __1 in nums.items():
    if __[:-1] not in ignore and __[:-1] != "":
        print(__[0:-1]+" раз "+str(__1))
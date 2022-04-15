from pandas import read_csv
import pandas as pd
import datetime

data = read_csv("ИПО\\apple_28.csv")
framepd = pd.DataFrame(data)

framepd.sort_values(by="Date", inplace =True) 

startAt = framepd["Date"][len(framepd["Date"])-1].split("-")

lastDayWeek = datetime.datetime(int(startAt[0]), int(startAt[1]), int(startAt[2]), 12, 0, 0)

print(framepd)

middleCLose = 0
weekdayLast = lastDayWeek.weekday()
weekCount = 0

for __ in framepd["Date"]:
	listTime = str(__).split("-")
	listDayWeek = datetime.datetime(int(listTime[0]), int(listTime[1]), int(listTime[2]), 12, 0, 0)
	middleCLose += float(framepd[framepd["Date"] == __]["Close"])
	print(str(listDayWeek.weekday()) + " " + str(lastDayWeek.weekday()))
	if listDayWeek.weekday() - lastDayWeek.weekday() <= 0:
		weekCount+=1
		print("Отчёт по неделе "+str(weekCount)+": "+str(middleCLose))
		middleCLose = 0
	lastDayWeek = datetime.datetime(int(listTime[0]), int(listTime[1]), int(listTime[2]), 12, 0, 0)
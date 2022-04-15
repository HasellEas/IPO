from pandas import read_csv
import pandas as pd

data = read_csv("ИПО\\apple_28.csv")
framepd = pd.DataFrame(data)

framepd.sort_values(by="Date", inplace =True)

count = 0

array = {
	"Open": 0,
	"High": 0,
	"Low": 0,
	"Close": 0,
	"Volume": 0,
	"Adj Close": 0
}

for __ in framepd["Date"]:
	if __ >= "2016-10-01" and __ <= "2017-02-31":
		framemomment = framepd[framepd["Date"] == __]
		for __ in framemomment:
			if __ != "Date":
				array[__] += float(framemomment[__])
				count += 1

print(framepd)

for __ in array.items():
	print(str(__[0]) + " = " + str(__[1]/count))
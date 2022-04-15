# s1.txt
# shop,selled,name
# 328,1,5элемент
# 325,2,электросила
# 365,3,зеон
# 985,4,21vek
# 125,5,евроторг

# s2.txt
# shop,marks,country
# 328,HP,США
# 325,Acer,Китай
# 365,Asus,Тайвань
# 985,Samsung,Корея
# 125,Dell,США

from pandas import read_csv
import pandas as pd

a = read_csv("s1.txt")
b = read_csv("s2.txt")

print("Задание 1, 2, 3")

print(a)
print(b)

print("\nЗадание 4")

a.loc[2 ,"name"] = "zeon"
print(a)

print("\nЗадание 5")

b.insert(loc=1,column="selled", value=a["selled"])

print(b)

print("\nЗадание 6")

tableS = pd.DataFrame({})
tableS.insert(loc=0,column="country",value=b["country"])
tableS.insert(loc=1,column="marks",value=b["marks"])
tableS.insert(loc=2,column="selled",value=a["selled"])

print(tableS)
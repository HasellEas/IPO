import pandas as pd

data = pd.MultiIndex.from_product([["Гомель", "Минск", "Брест", "Гродно", "Могилёв"],[2018,2019]])

dataPopul = pd.Series([1309890,1409890,1992800,2018281,1348115,1380391,1039278,1043681,1052746,1052877], index=data)

dataPopul.index.names = ["city", "year"]

form_flat = dataPopul.reset_index(name="population")

print(form_flat)
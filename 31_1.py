import pandas as pd
from pandas import read_csv

csv2 = pd.DataFrame(read_csv("state-abbrevs.csv"))

csv3 = pd.DataFrame(read_csv("state-population.csv"))

print(pd.concat([csv3["state/region"], csv2["abbreviation"]], axis=1))
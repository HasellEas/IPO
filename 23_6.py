import numpy as np
from ast import literal_eval

a = np.array(literal_eval(input("a: ")), float)
b = np.array(literal_eval(input("b: ")), float)
c = np.array(literal_eval(input("c: ")), float)

d = np.concatenate((a,b,c))

print(d)
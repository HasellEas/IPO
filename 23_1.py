import numpy as np
from ast import literal_eval

listing = (5,6,7,8,4)

a = np.array(literal_eval("["+str(listing)[1:-1]+"]"), int)

print(a)
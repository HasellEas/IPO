import numpy as np

a = np.array([6,2,0,3,0,0,5,7,0], float)

minarray = []

i = 0 

for __ in range(0, len(a)):
	if a[__] == 0:
		try:
			minarray.append(a[__+1])
		except:
			None
	i+=1

print(max(minarray))
	
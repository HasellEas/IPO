a = (67,248)

massive = []
for __ in range(1, 100):
	massive.append(a)
	a = (a[0]+1, a[1]-1)

print(massive)

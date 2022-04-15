import numpy

x = numpy.array([[1,0,1],[2,0,2],[3,0,3],[4,0,0]], int)

s = 0
for __ in x.diagonal():
	if __ != 0:
		s*=__

print(__)
from math import *
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
p = a+b+c
pp = p/2
s = sqrt(pp*(pp-a)*(pp-b)*(pp-c))
print("Периметр: "+str(p)+"\nПлощадь: "+str(s))
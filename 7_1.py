n = int(input("В каком пространстве происходит счисление? "))
a= []
b= []

for __ in range(0, n):
    a.append(int(input("a"+str(__+1)+": ")))
    b.append(int(input("b"+str(__+1)+": ")))

formula = "output = (("+str(a[0])+" - "+str(b[0])+")*2" 

for __ in range(1, n):
    formula+=" + ("+str(a[__])+" - "+str(b[__])+")*2"

formula += ")**0.5"

exec(formula)

print("Вывод "+str(output))
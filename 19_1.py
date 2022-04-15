import turtle as ts
t = ts.Pen()

ts.bgcolor("yellow")

t.fillcolor("green")
t.begin_fill()
for __ in range(0,4):
    t.forward(150)
    t.right(90)
t.end_fill()

input()
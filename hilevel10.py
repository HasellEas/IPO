import turtle as ts
t = ts.Pen()
import random

def set_circles(len_input):
	circles = []
	colors = ["yellow","red","blue"]
	for __ in range(0,3):
		circles.append(random.randint(0,len_input))
	for __ in range(0,len_input):
		if __ in circles:
			color_c = colors[random.randint(0,2)]
			t.fillcolor(color_c)
			t.begin_fill()
			t.color(color_c)
			t.circle(14)
			t.end_fill()
		t.color("green")
		t.forward(1)

t.color("green")

t.up()
t.goto(-200, -200)
t.down()

t.fillcolor("green")
t.begin_fill()
t.forward(400)
t.left(160)
t.forward(220)
t.left(41)
t.forward(219)
t.end_fill()

t.up()
t.goto(-200, -200)
t.down()

t.left(159)

set_circles(400)
t.left(160)
set_circles(220)
t.left(41)
set_circles(219)

t.up()
t.goto(-160,-125)
t.down()

t.left(159)

t.fillcolor("green")
t.begin_fill()
t.forward(320)
t.left(160)
t.forward(170)
t.left(41)
t.forward(170)
t.end_fill()

t.up()
t.goto(-160,-125)
t.down()

t.left(159)

set_circles(320)
t.left(160)
set_circles(170)
t.left(41)
set_circles(170)

t.up()
t.goto(-110,-64)
t.down()

t.left(159)

t.fillcolor("green")
t.begin_fill()
t.forward(230)
t.left(160)
t.forward(121)
t.left(41)
t.forward(121)
t.end_fill()

t.up()
t.goto(-110,-64)
t.down()

t.left(159)

set_circles(230)
t.left(160)
set_circles(121)
t.left(41)
set_circles(121)

input()
#program file
from ZhangFunctions import*
turtle.colormode(255)
turtle.bgcolor(250,200,0)
bob.color("yellow")
bob.begin_fill()
bob.speed(0)
for times in range(90):
    bob.forward(5)
    bob.right(2)
bob.end_fill()


jump(5,-5)
bob.color("brown")
bob.begin_fill()
for times in range(4):
    bob.forward(40)
    bob.right(120)    
bob.end_fill()

bob.color("black")
bob.pensize(9)
bob.forward(40)
bob.right(120)
bob.forward(40)


bob.left(58.9)
for times in range(90):
    bob.forward(5)
    bob.right(2)
bob.right(90)
bob.forward(280)
bob.left(80)
bob.forward(40)

bob.color(253,253,253)
bob.begin_fill()
jump(35,-45)
bob.circle(29.5)
bob.end_fill()

bob.color("black")
bob.begin_fill()
jump(30,-55)
bob.circle(15)
bob.end_fill()

bob.color(253,253,253)
bob.begin_fill()
jump(35,-45)
bob.circle(29.5)
bob.end_fill()

bob.color("black")
bob.begin_fill()
jump(30,-55)
bob.circle(15)
bob.end_fill()

bob.pensize(5)
jump(33.5,-45)
bob.circle(30)

"""""""""""""""'"""

bob.color("black")
bob.begin_fill()
jump(75,-55)
bob.circle(15)
bob.end_fill()

bob.color(253,253,253)
bob.begin_fill()
jump(80,-45)
bob.circle(29.5)
bob.end_fill()

bob.color("black")
bob.begin_fill()
jump(75,-55)
bob.circle(15)
bob.end_fill()

bob.pensize(5)
jump(78.5,-45)
bob.circle(30)

bob.begin_fill()
jump(30,-150)
bob.left(180)
curve()

bob.left(120)
curve()
bob.left(90)
bob.forward(9.8)
bob.end_fill()

jump(60,-160)
bob.color(230,0,0)
bob.begin_fill()
bob.circle(15)
bob.end_fill()

bob.color("black")
jump(45,-170)
for time in range(50):
    bob.forward(50)
    bob.right(90+times)


for times in range(90):
    bob.forward(5)
    bob.right(2)
bob.end_fill()


jump(5,-5)
bob.color("brown")
bob.begin_fill()
for times in range(4):
    bob.forward(40)
    bob.right(120)    
bob.end_fill()

bob.color("black")
bob.pensize(9)
bob.forward(40)
bob.right(120)
bob.forward(40)


bob.left(58.9)
for times in range(90):
    bob.forward(5)
    bob.right(2)
bob.right(90)
bob.forward(280)
bob.left(80)
bob.forward(40)

bob.color(253,253,253)
bob.begin_fill()
jump(-65,-45)
bob.circle(29.5)
bob.end_fill()

bob.color("black")
bob.begin_fill()
jump(-70,-55)
bob.circle(15)
bob.end_fill()

bob.color(253,253,253)
bob.begin_fill()
jump(-65,-45)
bob.circle(29.5)
bob.end_fill()

bob.color("black")
bob.begin_fill()
jump(-70,-55)
bob.circle(15)
bob.end_fill()

bob.pensize(5)
jump(-66.5,-45)
bob.circle(30)

bob.color("black")
bob.begin_fill()
jump(-25,-55)
bob.circle(15)
bob.end_fill()

bob.color(253,253,253)
bob.begin_fill()
jump(-20,-45)
bob.circle(29.5)
bob.end_fill()

bob.color("black")
bob.begin_fill()
jump(-25,-55)
bob.circle(15)
bob.end_fill()

bob.pensize(5)
jump(-21.5,-45)
bob.circle(30)

bob.begin_fill()
jump(-70,-150)
bob.left(180)
curve()

bob.left(120)
curve()
bob.left(90)
bob.forward(9.8)
bob.end_fill()

jump(-40,-160)
bob.color(230,0,0)
bob.begin_fill()
bob.circle(15)
bob.end_fill()

bob.color("black")
jump(-55,-170)
for time in range(50):
    bob.forward(50)
    bob.right(90+times)

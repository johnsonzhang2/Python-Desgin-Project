#function file
import turtle
bob = turtle.Turtle()

def polygon(sides,distance,c):
    bob.color(c)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
        bob.color()
    bob.end_fill()
        
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,color):
    for times in range(5):
        bob.forward(distance)
        bob.right(144)

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
def curve():
    for times in range(10):
        bob.forward(10)
        bob.left(5)


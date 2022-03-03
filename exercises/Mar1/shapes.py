# Author: Ahmed Al touqi
import turtle
import random
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("skyblue")
turtle.bgcolor("white")

def draw_square(x, y, width, color):
    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()
def draw_triangle(x, y, width, color):
    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()


draw_square(50, -100, 60, "cyan")

draw_square(150, -50, 100, "blue")

draw_square(-100, 50, 40, "teal")

draw_triangle(-200,100,30, "pink")


turtle.done()
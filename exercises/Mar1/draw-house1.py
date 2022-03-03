# Author: Ahmed Al touqi
import turtle
import random
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("skyblue")
turtle.bgcolor("skyblue")
pen.hideturtle()


def draw_square(x, y, width, color):
    draw_rect(x,y,width,width, color)
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
def draw_rect(x,y,length,width, color):
    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
        if i%2==0:
            pen.forward(width)
        else:
            pen.forward(length)
        pen.left(90)
    pen.end_fill()
def draw_circle(x,y,radius,color):
    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    

draw_square(-150,-200,300,"gold")
draw_triangle(-160,100,320,"red")
draw_rect(-30,-200,100,70,"red")
draw_circle(30,-145,5,"white")
turtle.done()
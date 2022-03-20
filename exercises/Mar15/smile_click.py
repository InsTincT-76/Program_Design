# Author: Ahmed Al touqi
import turtle
import random
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
turtle.bgcolor("white")
pen.hideturtle()

faceRadius = 30
def draw_face(x,y):
    draw_head(x,y)
    draw_eye(x-faceRadius*.4,y) #left eye
    draw_eye(x+faceRadius*.4,y) # right eye
    draw_mouth(x,y-faceRadius*.5)
    
    
def draw_head(x,y):
    set_pos(x,y-faceRadius)
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(faceRadius)
    pen.end_fill()
    
    
def draw_eye(x,y):
    eyeRadius=faceRadius/5
    set_pos(x, y- eyeRadius)
    pen.fillcolor("black")
    if random.randint(0,1)==0:
        pen.begin_fill()
        pen.circle(eyeRadius)
        pen.end_fill()

    else:
        set_pos(x-eyeRadius,y)
        pen.forward(eyeRadius*2)
        
        
def draw_mouth(x,y):
    mouthRadius = faceRadius*.5
    set_pos(x - mouthRadius * .85,y)
    pen.fillcolor("black")
    if random.randint(0,1)==0:
        pen.setheading(-60)
        pen.circle(mouthRadius,120)
        pen.setheading(0)
        
    else:
        set_pos(x, y-mouthRadius*.5)
        pen.fillcolor("gray")
        pen.begin_fill()
        pen.circle(mouthRadius/2)
        pen.end_fill()
    
def set_pos(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    
turtle.onscreenclick(draw_face)

turtle.done()
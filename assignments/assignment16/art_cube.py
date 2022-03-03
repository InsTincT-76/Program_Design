#Author: Ahmed Al touqi
from re import X
import turtle
import random
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("black")
turtle.bgcolor("skyblue")
pen.hideturtle()
colors=["blue", "red", "gold", "black","pink","white"]

def draw_triangle(width, color):
    
    pen.color(color)
    
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()
    
    
def draw_cube(x,y,size):
    pen.up()
    pen.setx(x)
    pen.sety(y)
    pen.down()

    
        
    for i in range(6):
        draw_triangle(size,random.choice(colors))
        pen.left(60)
        
        


for i in range (20):
    size=random.randint(50,100)
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    draw_cube(x,y,size)

turtle.done()
# Author: Ahmed Al touqi
import turtle
import random
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
turtle.bgcolor("lightgrey")
pen.hideturtle()


car_width=150
wheel_radius=20
carColor=["blue","red","orange","green","lavendar","teal"]

def draw_street():
    pen.up()
    pen.setpos(-turtle.window_width(),0)
    pen.down()
    
    for i in range(0,20):
        pen.pencolor("yellow")
        pen.forward(50)
        pen.up()
        pen.forward(50)
        pen.down()
    pen.up()   
def draw_car(x,y):
    pen.color("black")
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(random.choice(carColor))
    pen.begin_fill()
    for i in range (0,4):
        if i%2==0:
            pen.forward(car_width)
        else:
            pen.forward(car_width/3)
        pen.left(90)
    pen.end_fill()
    pen.fillcolor("grey")
    pen.up()
    pen.setpos(x+car_width*1/4,y-wheel_radius)
    pen.down()
    pen.begin_fill()
    pen.circle(wheel_radius)
    
    pen.up()
    pen.setpos(x+car_width*3/4,y-wheel_radius)
    pen.down()
    pen.circle(wheel_radius)
    pen.end_fill()
    pen.up()
        
 
    
    
        


draw_street()
turtle.onscreenclick(draw_car)
turtle.done()
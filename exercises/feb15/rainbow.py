# Author: Ahmed Al touqi
import turtle
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.width(20)
pen.color("black")

colors = ("Violet", "indigo", "blue", "green", "yellow", "orange", "red")
radius = turtle.window_width()//6
y=0

for color in colors:
    pen.up()
    pen.setposition(0,y)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-radius, 120)
    y+=20
    




turtle.done()
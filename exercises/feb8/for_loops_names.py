#Author Ahmed Altouqi
import turtle
import random
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
style = ("Arial", 12, "normal")
userName = turtle.textinput("Names", "Enter name:")
numNames = int(turtle.numinput("Names", "Enter Number of Names", 10, 1, 100))



for i in range (numNames):
    x = random.randint(- turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(- turtle.window_height()//2, turtle.window_height()//2)
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    turtle.colormode(255)
    pen.color(r,g,b)

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(userName, font = style)




turtle.done()
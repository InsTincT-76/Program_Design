#Author: Ahmed Al touqi
import turtle
pen = turtle.Turtle()
turtle.setup(800,800)
turtle.bgcolor("white")
pen.pensize(2)
pen.speed(.5)


xCor = []
yCor = []

coordinates = turtle.numinput("Coordinates", "Enter Number of coordinates")


for cor in range (int(coordinates)):
    x1 = turtle.numinput("X1", "Enter X coordinate(s)")
    xCor.append(x1)

    y1 = turtle.numinput("Y1", "Enter y coordinate(s)")
    yCor.append(y1)
    
    
    
for i in range (len(xCor)):
    pen.setpos(xCor[i],yCor[i])
    
    








turtle.done()
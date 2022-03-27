import turtle
import random
from webbrowser import get

turtle.setup(1000,300)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
turtle.bgcolor("skyblue")
pen.hideturtle()


def getScene():
    sceneItems = []
    with open("assignments/assignment20/scene.txt") as file:
        for line in file:
            sceneItem = line.replace("\n","").strip().lower()
            sceneItems.append(sceneItem)
            
        return sceneItems



def drawFlower(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    circleRadius=size
    pen.color("green")
    pen.left((90))
    pen.forward(circleRadius*6)
    pen.color("hot pink")
    pen.setheading(0)
    for i in range(12):
        pen.circle(circleRadius*1.5)
        pen.left(30)



def drawTree(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    treeRadius=size
    
    pen.color("brown")
    pen.fillcolor("brown")
    pen.begin_fill()

    for i in range(4):
        if i%2==0:
            pen.forward(treeRadius)

        else:
            pen.forward(treeRadius*3)
        pen.left(90)
                
    pen.end_fill()    
    pen.up()
    pen.setpos(x+(treeRadius/2),y+(treeRadius*3))
    pen.down()
    pen.color("green")
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(treeRadius*3)
    pen.end_fill()



listItems=getScene()
numItems= len(listItems)
y=0
spacing = turtle.window_width()/numItems
size=10
x=-turtle.window_width()/2 + spacing/2


for myItem in listItems:
    if myItem=="flower":
        drawFlower(x,y,size)
        
    else:
        drawTree(x,y,size)
    x+=spacing

turtle.done()
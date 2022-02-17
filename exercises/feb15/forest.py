# Author: Ahmed Al touqi
import turtle
import random
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
turtle.bgcolor("skyblue")

gridSize = int(turtle.numinput("Size", "Enter size", 5, 1, 10))
treeSquareWidth = turtle.window_width()//gridSize
trunkWidth = treeSquareWidth // 5
padding = (treeSquareWidth-trunkWidth)//2
treeTrunkHeight = trunkWidth* 3
leafRadius = trunkWidth

x = (-turtle.window_width()//2 + padding)
y = (-turtle.window_height()//2 + padding)
for row in range (gridSize):
    x = (-turtle.window_width()//2 + padding)

    for col in range(gridSize):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color("brown")
        pen.begin_fill()
        
        for i in range(4): #trunk
            if i % 2 ==0:
                pen.forward(trunkWidth)
            else:
                pen.forward(treeTrunkHeight)
            pen.left(90)
                    
                    
                    
        pen.end_fill()
        pen.up()
        pen.setpos(x+ trunkWidth //2 , y+ treeTrunkHeight * .8)
        pen.down()
        
        
        # leaves
        pen.color("green")
        pen.begin_fill()
        pen.circle(leafRadius)
        pen.end_fill()
        x+= treeSquareWidth

    y+=treeSquareWidth
    
turtle.done()
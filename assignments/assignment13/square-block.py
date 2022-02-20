# Author: Ahmed Al touqi
import turtle
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(1)
turtle.bgcolor("skyblue")
pen.hideturtle()

gridSize = int(turtle.numinput("Block", "Enter Numbers of rows", 5, 1, 10))
boxsquareWidth = turtle.window_width()//gridSize
boxWidth = boxsquareWidth / 2
colors =[]

for c in range (int(gridSize)):
    color = (turtle.textinput("Block", "Enter color"))
    colors.append(color)

for row in range (gridSize):
    pen.fillcolor(colors[row])
    x = (-turtle.window_width()//2 + turtle.window_width()//4)
    y = (-turtle.window_height()//2 + turtle.window_height()//4 + boxWidth* row)
    
    for col in range(gridSize):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        
        
        
        
        
                 
        pen.begin_fill()

        for i in range(4): 
                pen.forward(boxWidth)
                pen.left(90)
        pen.end_fill()

             
       
        x+=boxWidth


turtle.done()
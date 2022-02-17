# Author: Ahmed Al touqi
import turtle
import random
turtle.setup(800,400)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("red")
turtle.bgcolor("white")

x = - turtle.window_width()//2
y = - turtle.window_height()//2
stripesWidth = turtle.window_width()
stripesHeight = turtle.window_height()//13

#draw red stripes
for i in range(7):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    #draw stripe
    for i in range (4):
        if i % 2 == 0:   #if i is even
            pen.forward(stripesWidth)
        
        
        else:
            pen.forward(stripesHeight)
        pen.left(90)
    pen.end_fill()
        
    y += stripesHeight * 2 #Move up for next stripe

bluesquareWidth = turtle.window_width()//2.5
bluesquareHeight = turtle.window_height() * 7/13
a = -turtle.window_width()//2
z= -turtle.window_height()//2 + (turtle.window_height() - bluesquareHeight)
pen.up()
pen.setpos(a,z)
pen.down()
pen.color("blue")

pen.begin_fill()
for i in range (4):
    if i % 2 ==0:
        pen.forward(bluesquareWidth)
    else:
        pen.forward(bluesquareHeight)
        
    pen.left(90)
pen.end_fill()
        
        
        
        
        
        
        
#Star information
starBox6Width = bluesquareWidth / 6
starboxHeight = bluesquareHeight / 9
star6Padding = starBox6Width / 4
starWidth = starBox6Width / 2


a = -turtle.window_width()//2 + starWidth // 2
z= -turtle.window_height()//2 + (turtle.window_height() - bluesquareHeight + star6Padding)
pen.up()
pen.setpos(a , z)
pen.down()



z= -turtle.window_height()//2 + (turtle.window_height() - bluesquareHeight )

pen.left(36)
for row in range(6):
    a = -turtle.window_width()//2 + starWidth // 2
    pen.up()
    pen.setpos(a , z)
    pen.down()

    if row % 2 ==0:
        numStars = 6
    else:
        numStars = 5
        a+= starWidth /2 + star6Padding
        
    for col in range (numStars):
        x+=star6Padding
        pen.up()
        pen.setpos(a,z)
        pen.down()
        pen.color("white")
        pen.begin_fill()
        
        for i in range(5):
            pen.forward(starWidth)
            pen.left(144)
        pen.end_fill() 
        a += starWidth + star6Padding * 2

    
    z += starboxHeight+star6Padding

    
turtle.done()
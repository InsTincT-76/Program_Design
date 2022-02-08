#Author Ahmed Al touqi
import turtle
turtle.setup(900,800)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(8)
pen.color("magenta")

#Variables
hexSide = 90
x = turtle.window_width()//4
y = -turtle.window_height()//8


#Hex 1
pen.up()
pen.setpos(x,y)
pen.down()

pen.fillcolor("cyan")
pen.begin_fill()

for i in range(6):
    pen.forward(hexSide)
    pen.right(60)
    
pen.end_fill()
    
    
#Hex 2
pen.up()
pen.setpos(x-hexSide*1.5,y+hexSide*.85)
pen.down()

pen.fillcolor("cyan")
pen.begin_fill()

for i in range(6):
    pen.forward(hexSide)
    pen.right(60)
    
pen.end_fill()
    
    
#Hex 3
pen.up()
pen.setpos(x-hexSide*1.5 -hexSide*1.5,y+hexSide*.85 +hexSide*.85)
pen.down()

pen.fillcolor("cyan")
pen.begin_fill()

for i in range(6):
    pen.forward(hexSide)
    pen.right(60)
    
pen.end_fill()
    
    
#Hex 4
pen.up()
pen.setpos(x-hexSide*1.5 -hexSide*1.5 -hexSide*1.5 ,y+hexSide*.85 +hexSide*.85 + hexSide*.85)
pen.down()

pen.fillcolor("cyan")
pen.begin_fill()

for i in range(6):
    pen.forward(hexSide)
    pen.right(60)
    
pen.end_fill()

#Hex 5
pen.up()
pen.setpos(x-hexSide*1.5 -hexSide*1.5 -hexSide*1.5 -hexSide*1.5 ,y+hexSide*.85 +hexSide*.85 + hexSide*.85 + hexSide*0.85)
pen.down()

pen.fillcolor("cyan")
pen.begin_fill()
for i in range(6):
    pen.forward(hexSide)
    pen.right(60)
pen.end_fill()



turtle.done()
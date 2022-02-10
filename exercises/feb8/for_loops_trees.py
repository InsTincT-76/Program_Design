#Author Ahmed Altouqi
import turtle
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

trunkWidth = turtle.window_width() // 10
lgTriangle = trunkWidth * 3
mdTriangle = lgTriangle * 2/3
smTriangle = mdTriangle * 2/3
starWidth = smTriangle * .2
bottomY = -lgTriangle * 3/2
pen.up()
pen.setpos(-trunkWidth/2, -lgTriangle * 3/2)
pen.down()
#Trunk
pen.color("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(trunkWidth)
    pen.left(90)
pen.end_fill()  

pen.up()
pen.setpos(-lgTriangle/2, bottomY + trunkWidth)
pen.down()
pen.color("forest green")
#lg triangle
pen.begin_fill()
for i in range(3):
    pen.forward(lgTriangle)
    pen.left(120)
pen.end_fill()
    
pen.up()
pen.setpos(-mdTriangle/2, bottomY + trunkWidth + lgTriangle/2)
pen.down()
pen.color("forest green")
#md triangle
pen.begin_fill()
for i in range(3):
    pen.forward(mdTriangle)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-smTriangle/2, bottomY + trunkWidth + lgTriangle/2 + mdTriangle/2)
pen.down()
pen.color("forest green")
#sm triangle
pen.begin_fill()
for i in range(3):
    pen.forward(smTriangle)
    pen.left(120)
pen.end_fill()


pen.up()
pen.setpos(-starWidth/2, bottomY + trunkWidth + lgTriangle/2 + mdTriangle/2 + smTriangle)
pen.down()
pen.color("gold")
#star 
pen.begin_fill()
for i in range(3):
    pen.forward(starWidth)
    pen.right(120)
pen.end_fill()


pen.up()
pen.setpos(-starWidth/2, bottomY + trunkWidth + lgTriangle/2 + mdTriangle/2 + smTriangle - starWidth/2)
pen.down()
pen.color("gold")
#star 
pen.begin_fill()
for i in range(3):
    pen.forward(starWidth)
    pen.left(120)
pen.end_fill()

pen.hideturtle()
turtle.done()
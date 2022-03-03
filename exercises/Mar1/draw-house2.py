#Author: Ahmed Al touqi
import turtle
turtle.setup(800,800)
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("skyblue")
turtle.bgcolor("skyblue")
pen.hideturtle()


def draw_house(x,y, width, body_color, roof_color):
    draw_square(x-width/2,y-width/2,width, body_color)
    draw_triangle(x-width*.6,y+width/2, width*1.2,roof_color)
    draw_rect(x-width*.15,y-width/2,width*.3,width*.6,roof_color)
    draw_circle(x+width*.05,y-width*.15,width*.05,body_color)

def draw_square(x, y, width, color):
    draw_rect(x,y,width,width, color)
def draw_triangle(x, y, width, color):
    
    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()
def draw_rect(x,y,width,length, color):
    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
        if i%2==0:
            pen.forward(width)
        else:
            pen.forward(length)
        pen.left(90)
    pen.end_fill()
def draw_circle(x,y,radius,color):
    

    pen.up()
    pen.color(color)
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    
    

draw_house(-0,-100,80,"violet","gold")

draw_house(150,100,80,"blue","pink")

draw_house(-140,100,80,"red","orange")

draw_house(-140,-300,80,"orange","blue")

draw_house(150,-300,80,"yellow","green")







turtle.done()
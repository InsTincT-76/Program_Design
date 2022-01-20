#Author: Ahmed Altouqi
import turtle

turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)


#Draw circle 1
pen.penup()
pen.setpos(-100,-100)
pen.pendown()
pen.fillcolor("light pink")
pen.begin_fill()
pen.circle(50)
pen.end_fill()


#Draw bike
pen.penup()
pen.setheading(0)
pen.left(90)
pen.forward(50)
pen.right(90)
pen.pendown()
pen.forward(150)
pen.left(45)
pen.forward(150)
pen.setheading(0)
pen.left(180)
pen.forward(150)
pen.left(45)
pen.forward(150)
pen.penup()
pen.setpos(50,-50)
pen.pendown()
pen.setheading(0)
pen.left(113)
pen.forward(150)
pen.setheading(0)
pen.forward(30)
pen.left(180)
pen.forward(60)


#draw circle 2
pen.penup()
pen.setposition(200,-100)
pen.setheading(0)
pen.pendown()
pen.fillcolor("light pink")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

#Continue on bike
pen.setheading(0)
pen.penup()
pen.left(90)
pen.forward(50)
pen.pendown()
pen.left(23)
pen.forward(150)
pen.setheading(0)
pen.left(180)
pen.forward(30)



turtle.done()
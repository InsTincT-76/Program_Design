import turtle

turtle.bgcolor("skyblue")

pen = turtle.Turtle()

pen.pensize(10)
pen.speed(0)

#Draw a square

pen.pencolor("red")
pen.fillcolor("green")
pen.begin_fill()
pen.forward(300)
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(300)
pen.end_fill()
pen.penup()
pen.setpos(-200,300)

#Draw a circle
pen.pendown()
pen.circle(50)

#Draw a triangle
pen.penup()
pen.setheading(-90)
pen.forward(400)
pen.pendown()
pen.setheading(0)
pen.begin_fill()
pen.pencolor("yellow")
pen.fillcolor("yellow")
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.end_fill()

#backwards triangle
pen.penup()
pen.setposition(300,-400)
pen.pendown()
pen.color("blue")
pen.setheading(0)
pen.forward(-100)
pen.right(120)
pen.forward(-100)
pen.right(120)
pen.forward(-100)
turtle.done()
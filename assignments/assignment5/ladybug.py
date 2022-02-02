from cgitb import small
from cmd import PROMPT
import turtle

turtle.bgcolor("cornsilk")
turtle.setup="500,500"
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)


num = turtle.numinput("Ladybug", "Enter size 1-10" ,minval=1 ,maxval=10)

largeCircle = 30 * num
middleCircle = largeCircle * 1/8
smallCircle = largeCircle * 2/3
eyeSize = smallCircle * 0.15

#The back

pen.fillcolor("crimson")
pen.penup()
pen.sety(-largeCircle)
pen.setx(largeCircle *.5)
pen.pendown()
pen.begin_fill()
pen.circle(largeCircle)
pen.end_fill()

#dimple 1
pen.penup()
pen.setx(-largeCircle/8)
pen.sety(-largeCircle +largeCircle*2/5)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()

#dimple 2
pen.penup()
pen.setx(-largeCircle/8)
pen.sety(largeCircle -largeCircle*3/5)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()


#dimple 3
pen.penup()
pen.setx(largeCircle/2)
pen.sety(largeCircle - largeCircle*2/3)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()

#dimple 4
pen.penup()
pen.setx(largeCircle/2)
pen.sety(-largeCircle + largeCircle*1/3)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()

#dimple 5
pen.penup()
pen.setx(largeCircle + largeCircle/8)
pen.sety(-largeCircle +largeCircle*2/5)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()


#dimple 6
pen.penup()
pen.setx(largeCircle + largeCircle/8)
pen.sety(largeCircle - largeCircle*2/3)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()

#line on back
pen.penup()
pen.setpos(-largeCircle/2,-largeCircle*.5 + largeCircle*.5)
pen.pensize(10)
pen.color("dark green")
pen.down()
pen.forward(largeCircle*2)


#head
pen.pensize(2)
pen.color("dark green")
pen.penup()
pen.setpos(-largeCircle/2 + largeCircle*.25,-largeCircle*.5 + largeCircle*.5)
pen.left(90)
pen.pendown()
pen.fillcolor("dark green")
pen.begin_fill()
pen.circle(smallCircle)
pen.end_fill()
pen.setheading(0)
#eye1

pen.penup()
pen.setpos(-largeCircle/2 + largeCircle*.25 -smallCircle*2 + smallCircle*.40,-largeCircle*.5 + largeCircle*.5 - eyeSize*3)
pen.pendown()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

#eye2

pen.penup()
pen.setpos(-largeCircle/2 + largeCircle*.25 -smallCircle*2 + smallCircle*.40,-largeCircle*.5 + largeCircle*.5 + eyeSize)
pen.pendown()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()
pen.up()
pen.sety(largeCircle*3)

turtle.done()
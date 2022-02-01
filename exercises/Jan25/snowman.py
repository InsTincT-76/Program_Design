import turtle

turtle.bgcolor("skyblue")
turtle.setup="500,500"
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)

pen.fillcolor("white")



largeCircle = 75
middleCircle = largeCircle * 3/4
smallCircle = middleCircle * 3/4
eyeSize = smallCircle * 0.1
noseSize = smallCircle * 0.2

pen.sety(-largeCircle)
pen.begin_fill()
pen.circle(largeCircle)
pen.end_fill()

pen.up()
pen.sety(.5 * largeCircle)
pen.down()
pen.begin_fill()
pen.circle(middleCircle)
pen.end_fill()

pen.up()
pen.sety(.5 * largeCircle + 1.5 * middleCircle)
pen.down()
pen.begin_fill()
pen.circle(smallCircle)
pen.end_fill()

pen.fillcolor("black")
pen.up()
pen.sety(.5 * largeCircle + 1.5 * middleCircle + smallCircle)
pen.setx(-smallCircle * .3)
pen.down()
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

pen.fillcolor("black")
pen.up()
pen.sety(.5 * largeCircle + 1.5 * middleCircle + smallCircle)
pen.setx(smallCircle * .3)
pen.down()
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

pen.fillcolor("orange")
pen.up()
pen.sety(.5 * largeCircle + 1.5 * middleCircle + smallCircle * .7)
pen.setx(-noseSize * .5)
pen.down()
pen.begin_fill()
pen.setheading(0)
pen.color="orange"
pen.forward(noseSize)
pen.left(120)
pen.forward(noseSize)
pen.left(120)
pen.forward(noseSize)
pen.up()
pen.setpos(-100,-100)
pen.end_fill()



turtle.done()
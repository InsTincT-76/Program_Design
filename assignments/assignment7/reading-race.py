import turtle
turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
style = ("Arial", "40", "bold")


centRadius=150
numBooks = turtle.numinput("Reading log" , "How many books have you read this month:  ")


if numBooks >= 30:
    #circle
    pen.up()
    pen.setpos(0,-centRadius)
    pen.down()
    pen.color("dark goldenrod")
    pen.fillcolor("dark goldenrod")
    pen.begin_fill()
    pen.circle(centRadius)
    pen.end_fill()


    pen.up()
    pen.sety(centRadius/6.5-centRadius)
    pen.down()
    pen.color("tan")
    pen.fillcolor("tan")
    pen.begin_fill()
    pen.circle(centRadius*.85)
    pen.end_fill()
    pen.hideturtle()

    turtle.up()
    turtle.setx(-centRadius/5)
    turtle.sety(-centRadius/10)
    turtle.down()
    turtle.color("dark goldenrod")
    turtle.write("$10" , font = style)
    turtle.hideturtle()
    
elif numBooks >= 15 and numBooks < 30:
    
    #circle
    pen.up()
    pen.setpos(0,-centRadius)
    pen.down()
    pen.color("gray")
    pen.fillcolor("gray")
    pen.begin_fill()
    pen.circle(centRadius)
    pen.end_fill()


    pen.up()
    pen.sety(centRadius/6.5-centRadius)
    pen.down()
    pen.color("gainsboro")
    pen.fillcolor("gainsboro")
    pen.begin_fill()
    pen.circle(centRadius*.85)
    pen.end_fill()
    pen.hideturtle()

    turtle.up()
    turtle.setx(-centRadius/6)
    turtle.sety(-centRadius/10)
    turtle.down()
    turtle.color("gray")
    turtle.write("$5" , font = style)
    turtle.hideturtle()
    
    
elif numBooks >= 5 and numBooks < 15:
    
    #circle
    pen.up()
    pen.setpos(0,-centRadius)
    pen.down()
    pen.color("saddle brown")
    pen.fillcolor("saddle brown")
    pen.begin_fill()
    pen.circle(centRadius)
    pen.end_fill()


    pen.up()
    pen.sety(centRadius/6.5-centRadius)
    pen.down()
    pen.color("burlywood")
    pen.fillcolor("burlywood")
    pen.begin_fill()
    pen.circle(centRadius*.85)
    pen.end_fill()
    pen.hideturtle()

    turtle.up()
    turtle.setx(-centRadius/6)
    turtle.sety(-centRadius/10)
    turtle.down()
    turtle.color("saddle brown")
    turtle.write("$2" , font = style)
    turtle.hideturtle()
    
    
    
else:
    #circle
    pen.up()
    pen.setpos(0,-centRadius)
    pen.down()
    pen.color("red")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(centRadius)
    pen.end_fill()


    pen.up()
    pen.sety(centRadius/6.5-centRadius)
    pen.down()
    pen.color("white")
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(centRadius*.85)
    pen.end_fill()
    pen.hideturtle()

    turtle.up()
    turtle.setx(-centRadius/6)
    turtle.sety(-centRadius/10)
    turtle.down()
    turtle.color("red")
    turtle.write("$0" , font = style)
    turtle.hideturtle()
    
    
    
    
    
    
    
turtle.done()
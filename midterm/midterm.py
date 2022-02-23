# Author: Ahmed Al touqi
import turtle
import random

turtle.setup(1600,800)
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(1)
turtle.bgcolor("skyblue")


pen.up()
pen.setposition(-turtle.window_width()//6,turtle.window_height()//2.5)
pen.down()

pen.write("Car Traffic and description", font=("Arial", 40, "bold"))

carAmount = int(turtle.numinput("Cars", "Enter Numbers of Cars", 2, 1, 10))








#uhaul widths
if carAmount >=6:
    uHaulWidth = turtle.window_width()//carAmount/2
    
elif carAmount>=3 and carAmount<=5:
    uHaulWidth = turtle.window_width()//carAmount/2.5
    

else:
    uHaulWidth = turtle.window_width()//carAmount/4


if carAmount ==10:
    style = ("Arial", 12, "bold")

elif carAmount >=6 and carAmount<10:
    style = ("Arial", 14, "bold")

elif carAmount <=5 and carAmount>=2:
    style = ("Arial", 22, "bold")

else:
    style = ("Arial", 30, "bold")







uHaulBoxWidth = uHaulWidth * 3/4
uHaulCabWidth = uHaulWidth - uHaulBoxWidth


#U- Haul heights
uHaulHeight = uHaulWidth * 5/8
uHaulBoxHeight = uHaulHeight * 2/3
uHaulCabHeight = uHaulBoxHeight * 2/3
uHaulWheelRadius = (uHaulHeight - uHaulBoxHeight)/2

carColor=[]
carName=[]
cloudRadius=50
padding = carAmount*.1

for n in range(int(carAmount)):
    name = (turtle.textinput("Block", "Enter Car Name"))
    carName.append(name)
    
    
for c in range(int(carAmount)):
    color = (turtle.textinput("Block", "Enter color"))
    carColor.append(color)
        
        
#Clouds
pen.fillcolor("white")
pen.color("white")
pen.up()
pen.setposition(-turtle.window_width()//3,turtle.window_height()//4)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.up()
pen.setposition(-turtle.window_width()//3,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.up()
pen.setposition(-turtle.window_width()//3+cloudRadius,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius) 
pen.end_fill()

pen.up()
pen.setposition(-turtle.window_width()//3 - cloudRadius,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()





pen.fillcolor("white")
pen.color("white")
pen.up()
pen.setposition(-turtle.window_width()//22,turtle.window_height()//4)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.up()
pen.setposition(-turtle.window_width()//22,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.up()
pen.setposition(-turtle.window_width()//22+cloudRadius,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius) 
pen.end_fill()

pen.up()
pen.setposition(-turtle.window_width()//22 - cloudRadius,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()



pen.fillcolor("white")
pen.color("white")
pen.up()
pen.setposition(turtle.window_width()//4,turtle.window_height()//4)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.up()
pen.setposition(turtle.window_width()//4,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.up()
pen.setposition(turtle.window_width()//4+cloudRadius,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius) 
pen.end_fill()

pen.up()
pen.setposition(turtle.window_width()//4 - cloudRadius,turtle.window_height()//4-cloudRadius)
pen.down()
pen.begin_fill()

pen.circle(cloudRadius)
pen.end_fill()

pen.color("black")

pen.up()




if carAmount>=7:
    x=-turtle.window_width()//2.2 + padding +carAmount*2
elif carAmount==6:
        x=-turtle.window_width()//2.2 + padding +carAmount*2 +uHaulWidth
else:
        x=-turtle.window_width()//2.2 + padding +carAmount*2+uHaulWidth*1.5



y=-turtle.window_height()//2.5 +padding + uHaulCabHeight


for col in range(carAmount):
    pen.fillcolor(carColor[col])
    
    #y = random.randint(-turtle.window_height()//2, turtle.window_height()//2) to make Y random but since we are on a traffic road y must be the same
        
        


    #Uhaul box
    pen.up()
    pen.setpos(x-uHaulWidth/2,y-uHaulHeight/2 +uHaulWheelRadius*2)
    pen.down()
    pen.begin_fill()
    pen.forward(uHaulWidth)
    pen.left(90)
    pen.forward(uHaulCabHeight)
    pen.left(90)
    pen.forward(uHaulCabWidth)
    pen.right(90)
    pen.forward(uHaulBoxHeight-uHaulCabHeight)
    pen.left(90)
    pen.forward(uHaulBoxWidth)
    pen.left(90)
    pen.forward(uHaulBoxHeight)
    pen.end_fill()

    #Left wheel
    pen.up()
    pen.setpos(x-uHaulWidth/2 +uHaulWidth*1/3 -uHaulWheelRadius,y-uHaulHeight/2 + uHaulWheelRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(uHaulWheelRadius)
    pen.end_fill()


    #Right wheel
    pen.up()
    pen.setpos(x-uHaulWidth/2 + uHaulWidth*2/3 -uHaulWheelRadius,y-uHaulHeight/2 + uHaulWheelRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(uHaulWheelRadius)
    pen.end_fill()      

    
    pen.up()
    pen.setpos(x-uHaulWidth/2 +uHaulBoxWidth/6 ,y-uHaulHeight/2 +uHaulWheelRadius*2 +uHaulCabHeight*2) 
    pen.down()
    pen.write(carName[col], font=style)
    pen.up()
    pen.setpos(x-uHaulWidth/2,y-uHaulHeight/2 +uHaulWheelRadius*2)
    pen.down()
    pen.setheading(0)
    x+=carAmount+uHaulWidth+padding+uHaulBoxWidth
    
    

#Road
pen.fillcolor("black")
pen.up()
pen.setpos(-turtle.window_width()/2,-turtle.window_height()//2.5 +padding + uHaulCabHeight-uHaulHeight/2 )
pen.down()
pen.begin_fill()
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(-turtle.window_height())
pen.left(90)
pen.forward(turtle.window_width())
pen.end_fill()

turtle.done()
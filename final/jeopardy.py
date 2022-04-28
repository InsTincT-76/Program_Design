from turtle import *
import turtle
import random
import jeopardy
from question import Questions
            
def take_input(x,y):
    global input_char

    ws = turtle.Screen()
    x=turtle.textinput("Hang-man Game", "Enter a letter")
    if x!="":
        input_char=x[0]
    else:
        input_char=""
        
        

def main():
    
    global input_char
    input_char=""
    
    q=jeopardy.Questions("final/qustions.txt")
    question=q.get_question()
    ans=q.get_answer()
    
    ans_str=""
    incorrect_str=""
    
    for i in ans:
        if i!=' ':
            ans_str+="_ "
        if i==' ':
            ans_str+="  "
    
    

    turtle.TurtleScreen._RUNNING=True
    list=turtle.Turtle()
    list.speed(0)

    
    attempts=10
    ans_found=0

    while ans_found==0:
        list.penup()
        list.goto(0,200)
        list.hideturtle()

        list.write(question,font=("courier",20,"bold"),align="center")

        list.penup()
        list.goto(0,100)
        list.hideturtle()

        list.write(ans_str,font=("courier",20,"bold"),align="center")

        list.penup()
        list.goto(0,0)
        list.hideturtle()

        list.write("Incorrect | Attempts Left:"+str(attempts),font=("courier",20,"bold"),align="center")

        list.penup()
        list.goto(0,-50)
        list.hideturtle()

        list.write(incorrect_str,font=("courier",20),align="center")
        
        
        screen = Screen()
        screen.onscreenclick(take_input)
        
        new=[]
        for i in ans_str:
            new.append(i)
            
        if input_char!="":
            false_inp=1
            for i in range(len(ans)):
                if str.lower(input_char)==str.lower(ans[i]):
                    false_inp=0
                    new[i*2]=ans[i]
                    
            ans_str=''.join(new)
            
            if false_inp:
                replace=1
                for i in incorrect_str:
                    if i==input_char:
                        replace=0
                if replace:
                    attempts-=1
                    incorrect_str+=input_char+","
            input_char=""
            turtle.clearscreen()
                    
            sol_found=1
            for i in range(len(ans)):
                if new[i*2]!=ans[i]:
                    sol_found=0
            if sol_found:
                ans_found=1
            if attempts==0:
                ans_found=2
            
    
    turtle.clearscreen()

    if ans_found==1:
        list.penup()
        list.goto(0,200)
        list.hideturtle()

        list.write("YAY! You Won",font=("courier",20,"bold"),align="center")
    if ans_found==2:
        list.penup()
        list.goto(0,200)
        list.hideturtle()

        list.write("You Lost :(",font=("courier",20,"bold"),align="center")
        

    turtle.exitonclick()

if __name__ == "__main__":
    main()






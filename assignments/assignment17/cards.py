import random
def deal():
    
    cards = {
        "ace" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "10" : "10",
        "jack" : "10",
        "queen" : "10",
        "king" : "10",
    }
    
    num = random.randint(0,12)
    if num ==0:
        return 1
    
    
    elif num ==1:
        return 2
    
    
    elif num ==2:
        return 3
    
    elif num ==3:
        return 4
    
    elif num ==4:
        return 5
    
    elif num ==5:
        return 6
    
    elif num ==6:
        return 7
    
    elif num ==7:
        return 8
    
    elif num ==8:
        return 9
    
    elif num ==9:
        return 10
    
    elif num ==10:
        return 10
    
    elif num ==11:
        return 10
    
    elif num ==12:
        return 10
        
        
you_score=0
comp_score=0

while True:
    computer_card=deal()
    your_card=deal()
    
    print(f"Computer deals a Card: {computer_card}")

    print(f"You deal a Card: {your_card}")
    
    
    if your_card > computer_card:
        print("You won this round")
        you_score+=1
    
    elif computer_card > your_card:
        print("Computer won this round")
        comp_score+=1
    elif computer_card == your_card:
     print("Tie")
    

    command = input("Would you like to play another round (Y)es, or (N)o? ").lower().strip()
    
    if command == "n":
        break
    
    
    
print(f"Your score: {you_score}")
print(f"Computer score: {comp_score}")
print("Goodbye")

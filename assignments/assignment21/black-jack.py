import random


def get_score():
    with open("assignments/assignment21/score.txt") as file:
        lines = file.readlines()
        
        if not lines:
            return 0
        
        return int(lines.pop())
    
    
    

def save_score(score):
    with open("assignments/assignment21/score.txt","w") as file:
        file.write(f"{score}")
        
        
        
        
  
def play_round():
    handTotal = (random.randint(1,11)+random.randint(1,11))
    computerTotal= random.randint(14,23)

    print(f"Your Hand Total: {handTotal} ")
      
    while handTotal<=21:
        command = input("Do you want another card (Y)es or (N)o? ").lower().strip()
          
        if command =="y":
            handTotal += (random.randint(1,11))
            print(f"Your Hand Total: {handTotal} ")
          
        elif command =="n":
            break
              
              
    print(f"Computers Hand Total: {computerTotal} ")

      
    if handTotal < computerTotal:
        return 1
    
    elif computerTotal>21:
        return 1
      
    elif handTotal > computerTotal:
        return -1
    
    elif handTotal>21:
        return -1
    
    
    elif handTotal == computerTotal:
        return 0
        
    
    
    
    
    
    

print("Let's Play Blackjack")
score = get_score()
    
while True:
    command=input("(P)lay or (Q)uit:  ").lower().strip()
    round=play_round()
    
    if command == "q":
        break
        
        
    elif command != "p":
        print("invalid command")
        continue
        
        
    elif command =="p":    
        if round==1:
            score += 1 
            print("You win")
            print(f"your current score is {score}")

        elif round==-1:
            score =score -1
            print("You Lose")
            print(f"your current score is {score}")
        
        
        elif round==0:
            print("Tie")
            print(f"your current score is {score}")
        
print("Goodbye")
save_score(score)
        
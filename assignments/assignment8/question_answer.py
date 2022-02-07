print("Welcome to our Question Answer Game")


while True:
    question = input("Ask a yes or no question: ")
    import random
    from turtle import goto
    num = random.randint(1,3)
    if num ==1:
        print("yes")
     
    elif num==2:
        print("No")
    
    else:
        print("Maybe")
    
    command = input("Would you like to ask another question? (Y)es or (N)o ? ").lower().strip()
    
    if command == "y":
        continue
    
    else:
        break
    
print("Goodbye")
        


#Author: Ahmed Altouqi

def displayMultiples(num):
    ans=1
    for i in range(1,101):
        if i%num==0:
            print(i)
            
            


#Math Program
while True:
    userInput = input("(L)ist Multiples or (Q)uit: ").lower().strip()
    
    if userInput == "q":
        break
    
    elif userInput == "l":
        num = int(input("Enter number:  "))
        displayMultiples(num)
        
        
    else:
        print("Invalid Command.")
print("Goodbye")
            

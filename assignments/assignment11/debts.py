#Author: Ahmed Altouqi

debts = []
debtValue = []

print("List of Companies With Internship")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()
    

    if command == "q":
        break
    
    
    elif command =="r":
        print("Sorry, people don't really pay off their debts :) ")
        
        
    elif command =="a":
         debt = input("Enter Debt Name:  ")
         debts.append(debt)
         
         debtvalue = input("Enter Debt Amount:  ")
         debtValue.append(debtvalue)
         
    elif command =="v":
        for i in range(len(debts)):
            print(f"-{debts[i]}: ${debtValue[i]}")
    
        
print("Goodbye")
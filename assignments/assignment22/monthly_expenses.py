FILE_NAME = "assignments/assignment22/expenses.txt"


def writeExpenses(expenses):
    with open(FILE_NAME,"w") as file:
        for expense in expenses:
            file.write(f"{expense}: {expenses[expense]} \n")
            
            
def read_Expenses():
    expenses={}
    with open(FILE_NAME) as file:
        for line in file:
            data=line.split(':')
            expense=data[0].strip()
            cost=data[1].strip()
            expenses[expense] = cost
    return expenses



def list_expenses(expenses):
    for expense in expenses:
        print(f"{expense}:${expenses[expense]}")            
        
    return expenses


def addExpense(expenses):
    expense = (input("Expense: "))
    cost= (input("Cost: "))
    expenses[expense] = cost
    
    return expenses


expenses=read_Expenses() 

while True:
    command = input("Enter (L)ist, (A)dd or (Q)uit. ")
    
    if command =="q":
        break
    
 

    elif command =="l":
        list_expenses(expenses)
        
    elif command =="a":
        expenses=addExpense(expenses)
        
        


print("Goodbye")
writeExpenses(expenses)        




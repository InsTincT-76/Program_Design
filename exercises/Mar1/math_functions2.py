#Author: Ahmed Altouqi

def factorial(num):
    ans=1
    for i in range(1,num+1):
        ans *=i
    print(f"{num}! = {ans}")
def sum(num):
    answer=0
    for i in range(1,num+1):
        answer+=i
    
    print(f"sum 1 to {num} = {answer}")       
def power(base, exp):
    anss=1
    for i in range(exp):
        anss*=base
        
    print(f"{base}^{exp}={anss}")
def is_prime(num):
    for i in range(2, num):
        if num % i ==0:
            print(f"{num} is not prime")
            return
        
    print(f"{num} is prime")
    
    
    
    
#Math Program
print("Welcome to my math game!!!")
while True:
    userInput = input("Enter (S)um, (P)ower, (F)actorial, (Pr)ime, or (Q)uit: ").lower().strip()
    
    if userInput == "q":
        break
    
    elif userInput == "s":
        num = int(input("Enter number:  "))
        sum(num)
    
    elif userInput == "p":
        base = int(input("Enter base:  "))
        exp = int(input("Enter exponent: "))
        power(base, exp)
        
        
    elif userInput == "f":
        num = int(input("Enter number: "))
        factorial(num)
        
        
    elif userInput == "pr":
        num = int(input("Enter Number: "))
        is_prime(num)
        
    else:
        print("Invalid Command.")
print("Goodbye")
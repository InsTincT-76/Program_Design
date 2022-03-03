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
    
is_prime(12)
is_prime(11)
#Author: Ahmed Altouqi

def factorial(num):
    ans=1
    for i in range(1,num+1):
        ans *=i
    return ans    
    
result = factorial(5)

print(f"5! = {result}")
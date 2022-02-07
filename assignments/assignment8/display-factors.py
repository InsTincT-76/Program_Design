print("let's count Factors")

num = int(input("Enter Number:  "))

i = 1
while i<=num:
    if num%i==0:
        print(-i)
    i = i+1
import random
print("Rolling dice Game")


while True:
    if input("Do you want to roll? ").lower().strip() != "y":
        break
    print(random.randint(1,6))
    

print("Goodbye")
        


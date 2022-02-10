toys = ["car", "truck" , "doll" , "train" , "lego"]

print("Welcome to our toy store")

while True:
    command = input("(V)iew , (A)dd, (R)emove, (Q)uit:  ")
    
    
    if command == "q":
        break
    
    elif command == "a":
        toy = input("Enter Toy:  ")
        toys.append(toy)
        print(f"{toy} was added")
        
        
    elif command == "r":
        toy = input("Enter Toy:  ")
        toys.remove(toy)
        print(f"{toy} was removed")
     
    
    elif command == "v":
        for i in range(len(toys)):
            print(f"{i+1}.  {toys[i]}")
        
        
    else:
        print("Invalid command")
        
    


print("Goodbye")
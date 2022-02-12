shoes = []

print("Shoe inventory")

while True:
    
    shoe = input("Enter Shoe Name:  ")
    shoes.append(shoe)
    
    
    command = input("Do you have more shoes to add, (Y)es or (N)o:  ").lower().strip()
    
    if command =="n":
        break
    
    elif command=="y":
        continue
    
    else:
        print("invalid command please try again")
    
print("Here's your shoe inventory list:")
for i in range(len(shoes)):
            print(f"{i+1}.  {shoes[i]}")



def get_friends():
    
    friends = []
    
    with open("exercises/Mar22/friends.txt") as file:
        for line in file:
            friends.append(line.strip().lower())
        return friends
            
#Display list of friends



print("Party Time")
people = get_friends()           


while True:
    command = input("(C)heck Guests, (L)ist guests, (Q)uit:  ").lower().strip()
    
    if command =="q":
        break
    
    
    
    elif command =="c":
        name = input("Enter Name:  ").lower().strip()
        if name in people:
            print("Welcome")
            
        else:
            print("Sorry you are not invited.")
            
    elif command =="l":
        for i in people:
            print(i)
            
print("Goodbye")
from pickle import TRUE


def get_phone_book():
    phone_list = {}
    with open("exercises/Mar22/phones.txt") as file:
        for line in file:
            data=line.split(',')
            name= data[0].lower().strip()
            phone=data[1].strip()
            phone_list[name] = phone
    return phone_list


def display_phone_book(phoneBook):
    for name in phoneBook:
        print(f"{name}: {phoneBook[name]}")
        
        

def display_phone_number(phoneBook, name):
    cleanName=name.lower().strip()
    if cleanName in phoneBook:
        print(f"{name}'s number is {phoneBook[cleanName]}")
        
    else:
        print(f"sorry {name} is not in our phone book")
        
        
        
      
phoneBook= get_phone_book()

while True:
    command = input("(V)iew, get (N)umber, (Q)uit").strip().lower()
    
    if command =="v":
        display_phone_book(phoneBook)
        
    elif command =="n":
        name= input("Enter Name:  ")
        display_phone_number(phoneBook, name)
        
    elif command == "q":
        break

    else:
        print("Sorry, that's an invalid command")
    
print("Goodbye")


        
        
        
        

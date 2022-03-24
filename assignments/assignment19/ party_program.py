def getBoolean(item):
    if item =="true":
        return True
    else:
        return False
def getGuests():
    guest_list = {}
    with open("assignments/assignment19/guest_list.txt") as file:
        for line in file:
            data=line.split(',')
            keys= data[0].lower().strip()
            values=data[1].strip()
            values = getBoolean(values)
            guest_list[keys] = values
    return guest_list
def displayGuests(guests, coming):
    for guest in guests:
        if guests[guest] == coming:
            print(f"-{guest}")
            
            
            

guestList=getGuests()    




while True:
    command = input("View (A)ttending, (N)ot attending, or (Q)uit:  ").strip().lower()
    
    if command =="a":
        displayGuests(guestList,True)
        
    elif command =="n":
        displayGuests(guestList,False)
        
    elif command == "q":
        break

    else:
        print("Sorry, that's an invalid command")
    
print("Goodbye")

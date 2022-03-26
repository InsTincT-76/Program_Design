def getPrice():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Invalid number")
            
            
        
        
def getQuantity():
    while True: 
        try:
            quantity = int(input("Enter quantity:  "))
            return quantity
        except ValueError:
            print("Invalid whole number")
            
            
# Our calculator 
print("Our cost calculator")

price = getPrice()
quantity = getQuantity()
total = price * quantity
print(f"Your total is ${round(total,2)}")
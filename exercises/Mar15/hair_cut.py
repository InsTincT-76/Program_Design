def get_cut_cost(gender,length, density):
    total=0
    if gender == "m":
        total+=20
    elif gender =="f":
        total+=40

    if length == "s":
            total+=0
    elif length =="l":
        total+=10
        
        
    if density == "t":
            total+=15
    else:
        total+=0

    return total
def get_color_cost(length, density, change):
    total = 50
    
    if length =="l":
        total+=20
        
    if density =="t":
        total+=20
        
    if change =="l":
        total+=40
        
    
    return total



print("Salon Calculator")


Gender=input("Enter your Gender (M)ale or (F)emale: ").lower().strip()
Hair_Length=input("Enter hair length (L)ong or (S)hort: ").lower().strip()
Hair_Density=input("Enter hair density (F)ine or (T)hick: ").lower().strip()
Hair_Cut=input("Would you like a hair cut (Y)es or (N)o: ").lower().strip()
Hair_Color=input("Would you like to change hair color (Y)es or (N)o: ").lower().strip()

cost=0
if Hair_Cut =="y":
    cost += get_cut_cost(Gender,Hair_Length,Hair_Density)
    
    
if Hair_Color =="y":
    change = input("(L)ighter or (D)arker? ").lower().strip()
    cost += get_color_cost(Hair_Length, Hair_Density, change)
    
cost*=1.07

print(f"Your estimated cost is ${round(cost, 2)}")
    







    
    
    
    
    
    
    
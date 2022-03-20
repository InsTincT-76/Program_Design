def farh_to_celc(farenheit):
    celcius=(farenheit-32)*5/9
    return celcius
def celc_to_farh(celcius):
    farenheit=celcius *9/5 + 32
    return farenheit
def miles_to_kilo(miles):
    kilometers=miles*1.60934
    return kilometers
def kilo_to_miles(kilometers):
    miles=kilometers*0.621371
    return miles





command = int(input(f"""
Enter type of conversion:
1.Farenheit to Celcius
2.Celcius to Farenheit
3.Miles to kilometers
4.Kilometers to miles:  """))


value = float(input("Enter Value:  "))

if command ==1:
    ftoc = farh_to_celc(value)
    print(f"{value}F = {round(ftoc,1)}C")
    
    
elif command ==2:
    ctof = celc_to_farh(value)
    print(f"{value}C = {round(ctof,1)}F")
    
elif command ==3:
    mtk = miles_to_kilo(value)
    print(f"{value}M = {round(mtk,1)}Km")
    
elif command ==4:
    ktm = kilo_to_miles(value)
    print(f"{value}Km = {round(ktm,1)}M")
    
else:
    print("Invalid command")
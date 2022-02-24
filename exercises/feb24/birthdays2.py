from datetime import date

birthdays = {
    
    "Amy" : date(2022, 11, 1) , 
    "Bobby" :date(2023, 1 , 22), 
    "Carlie" :date(2022, 3, 14), 
    "Dave" :date(2022, 7, 11), 
    "Erin" :date(2022, 8, 18), 
    "Frank" :date(2022, 5, 2)
}


for friends in birthdays:
    daysTill = (birthdays[friends] - date.today()).days
    print(f"{friends} - {daysTill} days away")
    
from datetime import date, datetime, time


Exams = {
    "CSCE 204" : datetime(2022,2,25, 8, 30) , 
    "ITEC 362" : datetime(2022,2,25, 15, 00) , 
    "CHEM 105" : datetime(2022,2,26,8,30 ) , 
    "CHEM 107" : datetime(2022,2,26, 12,00) , 
    "STAT 201" : datetime(2022,2,28,15,30) , 
    "ITEC 101" : datetime(2022,2,28,16,45) , 
    "ITEC 233" : datetime(2022,3,1,11,20) , 
}



print("\n")

print("Todays Exams :")
for exam in Exams:
    if datetime.today().date() == Exams[exam].date():
        
        print(f"{Exams[exam].strftime('%I:%M %p')} {exam} ")
        
        
print("\n")

        
    
print("Upcoming Exams :")
for exam in Exams:
    if datetime.today().date() < Exams[exam].date():
        
        print(f"{Exams[exam].strftime('%I:%M %p')} {exam} ")
        
    


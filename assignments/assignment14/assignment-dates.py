from datetime import date, datetime


assignments = {
    "Assignment 1 - Intro" : date(2021,12,7) , 
    "Assignment 2 - Mad Libs" : date(2021,12,5) , 
    "Assignment 3 - Bike" : date(2021,12,8) , 
    "Assignment 4 - Prices" : date(2022,2,12) , 
    "Assignment 5 - LadyBug" : date(2022,2,25) , 
    "Assignment 6 - Zodiac Signs" : date(2022,2,27) , 
    "Assignment 7 - Reading Race" : date(2022,3,7) , 
    "Assignment 8 - Count Factors" : date(2022,3,15) , 
    "Assignment 9 - Hexagon" : date(2022,3,24) , 
    "Assignment 10 - Shoes" : date(2022,3,28) , 
    
}



for assignment in assignments:
    daysTill = (assignments[assignment] - date.today()).days
    if daysTill < 0:
        DaysTill = abs(daysTill)
        print(f"{assignment} - {assignments[assignment].strftime('%b %d, %A')} - {DaysTill} days past due")
    elif daysTill ==0:
                print(f"{assignment} - {assignments[assignment].strftime('%b %d, %A')} - due today! ")
                
    elif daysTill <= 15 and daysTill >0:
                        print(f"{assignment} - {assignments[assignment].strftime('%b %d, %A')} - due in {daysTill} days ")

    else:
        print(f"{assignment} - {assignments[assignment].strftime('%b %d, %A')}")

        

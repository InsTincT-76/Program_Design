from datetime import time


assignments = {
    "Assignment 1" : time(9,45) , 
    "Assignment 2" : time(12,0) , 
    "Assignment 3" : time(14,30) , 
    "Assignment 4" : time(18,45) , 
    "Assignment 5" : time(22,0) , 
    
    
}


for assignment in assignments:
    Time = assignments[assignment]
    print(f"{assignment} is due at {Time.strftime('%I:%M %p')}")

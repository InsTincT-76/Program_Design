#Author: Ahmed Al touqi
print(f"Lets calculate your grade.")

assignments = float(input("Enter your Assignments Grade: "))
exercises = float(input("Enter your Exercises Grade: "))
midterm = float(input("Enter your Midterm Grade: "))
final = float(input("Enter your Final Grade: "))

class_grade = assignments * .55 + exercises * .15 + midterm * .15 + final * .15
print(f"Your grade is {round(class_grade, 1)}")
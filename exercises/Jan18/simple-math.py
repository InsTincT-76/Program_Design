#Author: Ahmed Al touqi
import math

# Incrementing Age
age = float(input("Enter age: "))
decade = 10
future_age = age + decade
print(f"Your future Age is {future_age}")

#Pizza Party
print(f"We're having a pizza party!")
num_guests = int(input("Enter number of guests: "))
num_slices = float(input("Enter Average slices per guest: "))
total_slices = num_guests * num_slices
num_pizza = math.ciel(total_slices / 8)
print(f"You should order {num_pizza} !")

# Chickens and Eggs
num_eggs = int(input("How many eggs did you collect today: "))
num_cartons = num_eggs // 12   #Round down
eggs_left = num_eggs % 12 
print(f"You have {eggs_left} eggs left over")

#Hourly wage
wage_hourly = float(input("How much do you get paid hourly: $"))
wage_hourly *= 1.5
print(f"You should make ${round(wage_hourly, 2)} in overtime. ") #Rounds to 2 decimal places.

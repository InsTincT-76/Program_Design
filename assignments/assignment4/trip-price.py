#Author: Ahmed Al touqi
import math

print(f"let's see how expensive your road trip will be")
num_miles = float(input("How many miles will you travel: "))
num_days = int(input("How many days will you be traveling: "))
price_gallon = 3.159
miles_gallon = 24.9
breakfast_cost = 10 * num_days
lunch_cost = 12.50 * num_days
dinner_cost = 20 * num_days
hotel_cost = 103.25 * num_days
price_gas = num_miles / miles_gallon * price_gallon
travel_cost = price_gas + breakfast_cost + lunch_cost + dinner_cost + hotel_cost
print(f"Your travel cost is: ${round(travel_cost, 2)}")

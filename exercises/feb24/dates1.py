from datetime import date, time, datetime

todaysDate = date.today()

print(todaysDate)
print(todaysDate.strftime("%A  %b %dth, %Y"))


halloween = date(2022, 10, 31)
print(halloween.strftime("%m/%d/%Y"))



classTime = time(8, 30)

print(classTime.strftime("%I:%M %p"))


pieDay = datetime(2022, 3, 14, 13, 59)
print(pieDay.strftime("%m.%d.%I.%M"))




birthdayText = input("Enter Birthday (MM/DD/YYYY)").strip()
birthday = datetime.strptime(birthdayText, "%m/%d/%Y")

print("Your birthday is " + birthday.strftime("%B %d"))


# how long till pie day

daysTillPie = (pieDay - datetime.now()).days

print(f"You have {daysTillPie} days till pie day")

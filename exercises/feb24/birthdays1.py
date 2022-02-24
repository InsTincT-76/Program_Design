from datetime import date


birthdays = [date(2022, 11, 1) , date(2023, 1 , 22), date(2022, 3, 14), date(2022, 7, 11), date(2022, 8, 18), date(2022, 5, 2)]

for birthday in (birthdays):
    daysAway = (birthday - date.today()).days
    print(f"{birthday.strftime('%B %d')} - {daysAway} days away!")
    
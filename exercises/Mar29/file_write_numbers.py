numbers = [8,16,43,87]

with open("exercises/Mar29/numbers.txt","w") as file:
    for number in numbers:
        file.write(f"{number}\n")


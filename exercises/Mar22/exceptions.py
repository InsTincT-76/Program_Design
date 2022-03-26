from readline import read_init_file


try:
    number = int(input("Enter number:  "))
except ValueError:
    print("you entered an invalid integer")
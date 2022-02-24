toys = {
    "doll" : 19.89,
    "car" : 1.99,
    "truck" : 7.85,
    "puzzle" : 14.98,
    "slinky" : 2
}


#print(toys["truck"])
toys["yo-yo"] = 4.5

toyName = input("Enter a toy name").strip().lower()
print(f"{toyName} costs ${toys[toyName]}")

#Display all the toys


for toyName in toys:
    print(f"{toyName} costs %{toys[toyName]}")
    
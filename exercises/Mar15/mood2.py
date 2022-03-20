def get_mood(color):
    if color=="red":
        return "angry"
    
    elif color=="yellow":
        return "mellow"
    
    elif color=="blue":
        return "sad"
    
    elif color=="green":
        return "happy"
    
    elif color=="black":
        return "scary"
    
    elif color=="purple":
        return "royal"
    
    elif color=="pink":
        return "fun"
    
    
while True:
    print("Mood Ring!")
    colors = input("Enter Color: ")
    mood = get_mood(colors)
    print(f"You are feeling {mood}")

    command = input("Would you like to play again (Y)es or (N)o? ").lower().strip()
    if command !="y" and command !="yes":
        break
    
print("Goodbye")
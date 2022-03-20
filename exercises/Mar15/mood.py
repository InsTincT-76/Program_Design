def get_mood(color):
    mood_chart = {
        "red" : "angry",
        "yellow" : "mellow",
        "blue" : "sad",
        "green" : "happy",
        "black" : "scary",
        "purple" : "royal",
        "pink" : "fun"
    }
    
    color = color.strip().lower()    
    
    if color in mood_chart:
        return mood_chart[color]
    
    else:
        return "Confused"
    
print(get_mood("blue"))
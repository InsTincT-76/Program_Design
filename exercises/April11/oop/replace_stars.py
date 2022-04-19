def replace_stars():
    answer = ""
    global word    #only use global when its neccessary.
    for letter in word:
        if letter == "*":
            answer += "."
            
        else:
            answer += letter
            
    word= answer

word="a*b*c*d*"
replace_stars()
print(word)
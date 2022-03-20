import random


def roll():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total = dice1 + dice2
    print(f"{dice1}, {dice2}, total: {total}")
    return total


print("Let's decide who goes first")

print("player 1 rolls:")
player1Total = roll()

print("player 2 rolls:")
player2Total = roll()




if player1Total > player2Total:
    print("Player 1 goes first")
    
elif player2Total > player1Total:
    print("Player 2 goes first")    
    
else:
    print("Tie")
    
import random


def roll():
    return random.randint(1,6)


print("Let's decide who goes first")

player1dice1 = roll()
player1dice2 = roll()
player1Total = player1dice1 + player1dice2



player2dice1 = roll()
player2dice2 = roll()
player2Total = player2dice1 + player2dice2



print(f"Player 1 rolls {player1dice1} and {player1dice2} = {player1Total}")
print(f"Player 2 rolls {player2dice1} and {player2dice2} = {player2Total}")



if player1Total > player2Total:
    print("Player 1 goes first")
    
elif player2Total > player1Total:
    print("Player 2 goes first")    
    
else:
    print("Tie")
    
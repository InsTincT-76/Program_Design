friends = ["Amy","Beth","Carl","Dave"]


with open("exercises/Mar29/friends.txt","w") as file:
    for friend in friends:
        file.write(f"{friend}\n")
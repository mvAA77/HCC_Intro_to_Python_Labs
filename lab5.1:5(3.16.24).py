## Introduction
print("Soccor Calculator")
enter = input("Would You Like To Enter A Game? Y/N: ")

## Initializes variables for calculation
totalGames = 0
totalShots = 0
totalGoals = 0

## Input Validation and Error Display Fuction. Returns the input mumber if it passes the validation
def userInput(topic):
    num = input(f"Enter Total Number of {topic}: ")
    num = int(num)
    if num < 0:
        print(f"Error - {topic} cannot be a negative number. Try again")
        num = float(input(f"Enter Total Number of {topic} Played: "))
    return num


while enter == "Y" or enter == "y":

    # Takes the input of the user's games, shots, and goals
    print("\n") # White Space
    totalGames = userInput("Games")
    if totalGames == 0:
        print(f'Average Goals per Game is: {totalGames:.2f}')
        #Average Shots per Game
        print(f'Average Shots per Game is: {totalGames:.2f}')
        #Average Shots per Goal
        print(f'Average Goals per Game is: {totalGames:.2f}')
    else:
        print("\n")
        totalShots = userInput("Shots")
        print("\n")
        totalGoals = userInput("Goals")

    # Calculates and prints the average goals per game, average shots per game
    # and average shots per goal
    # White Space
    print("\n")
    if totalGames > 0:
        #Average Goals per Game
        ## Average Goals 
        if totalGoals > 0:
            print(f'Average Goals per Game is:  {(totalGoals / totalGames):.2f}')
            print(f'Average Shots per Goal is: {(totalShots / totalGoals):.2f}')
        else:
            print(f'Average Goals per Game is:  {totalGoals:.2f}')
            print(f'Average Shots per Goal is: {totalGoals:.2f}')
        #Average Shots per Game
        print(f'Average Shots per Game is:  {(totalShots / totalGames):.2f}')
    else:
        print("Please Reload To Enter Other Inputs")

    print("\n")# White Space
    enter = input("Would You Like To Play Another Game? Y/N: ")


if enter == "N" or enter == "n":
    # Prints goodbye
    print("Thank You For Your Time")


print("Soccor Calculator")
enter = input("Would You Like To Enter A Game? Y/N: ")
while enter == "Y" or enter == "y":

    # Takes the input of the user's games, shots, and goals
    print("\n") # White Space
    totalGames = input("Enter Total Number of Games Played: ")
    totalGames = float(totalGames)
    while totalGames < 0:
        print("Games Cannot Be Less Than Zero")
        totalGames = input("Enter Total Number of Games Played: ")
        totalGames = float(totalGames)
    
    totalShots = 0
    totalGoals = 0
    if totalGames <= 0:
        print(f'Average Goals per Game is: {totalGames:.2f}')
        #Average Shots per Game
        print(f'Average Shots per Game is: {totalGames:.2f}')
        #Average Shots per Goal
        print(f'Average Goals per Game is: {totalGames:.2f}')
    else:
        print("\n")
        totalShots = input("Enter Total Number of Shots Taken: ")
        totalShots = float(totalShots)
        while totalShots < 0:
            print("Shots Cannot Be Less Than Zero")
            totalShots = input("Enter Total Number of Shots Played: ")
            totalShots = float(totalShots)
        print("\n")
        totalGoals = input("Enter Total Number of Goals Scored: ")
        totalGoals = float(totalGoals)
        while totalGoals < 0:
            print("Goals Cannot Be Less Than Zero")
            totalGoals = input("Enter Total Number of Goals Played: ")
            totalGoals = float(totalGoals)

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

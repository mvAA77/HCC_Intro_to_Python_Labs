print("Soccor Calculator")
# Takes the input of the user's games, shots, and goals
print("\n") # White Space
totalGames = input("Enter Total Number of Games Played: ")
totalShots = input("Enter Total Number of Shots Taken: ")
totalGoals = input("Enter Total Number of Goals Scored: ")

# Converts the user inputs from a string to an integer and assigns the integer
# to their respective variables
totalGames = float(totalGames)
totalShots = float(totalShots)
totalGoals = float(totalGoals)

# Calculates and prints the average goals per game, average shots per game
# and average shots per goal
# White Space
print("\n")
#Average Goals per Game
print(f'Average Goals per Game is:  {(totalGoals / totalGames):.2f}')
#Average Shots per Game
print(f'Average Shots per Game is:  {(totalShots / totalGames):.2f}')
#Average Shots per Goal
print(f'Average Goals per Game is: {(totalShots / totalGoals):.2f}')

print("\n")# White Space
# Prints goodbye
print("Thank You For Your Time")

## Celsius to Fahrenheit Converter: Functions

## Displays the user control menu. Gets and returns the user choice
def menu():
    print("Temperature Converter")
    print("\n")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    choice = int(input("Please Enter Your Choice: "))
    if choice < 1 or choice > 3:
        print("\n")
        print("Error. Invalid Input. Please Try Again")
        choice = int(input("Please Enter Your Choice: "))
    return choice

## Gets the celsius temperature from the user and converts to fahrenheit
def to_fahr(ctemp):
    ftemp = (9/5) * ctemp + 32
    return ftemp

## Gets the fahrenheit temperature from the user and converts to celsius
def to_cels(ftemp):
    ctemp = (ftemp - 32) * 5/9
    return ctemp

## Displays menu and gets user input
menuReturn = menu()

## Initializes temperture output variables
temp = 0
newTemp = 0

## Runs calculator functions when user inputs "1" or "2"
while menuReturn == 1 or menuReturn == 2:
    if menuReturn == 1:
        print("\n")
        temp = float(input("Please Enter a Temperature in Celsius: ")) ## Gets Celsius Temperature
        ## User validation to prevent number input under absolute zero
        while temp < -273.15:
            print("\n")
            print("Error: Temperature Below Absolute Zero. Please Try Again")
            temp = float(input("Please Enter a Temperature in Celsius: "))
        ## Calls conversion function
        newTemp = to_fahr(temp)
        print("\n")
        ## Prints output
        print(f"The Temperature in Fahrenheit is {newTemp:.2f}")
    elif menuReturn == 2:
        print("\n")
        temp = float(input("Please Enter a Temperature in Fahrenheit: ")) ## Gets Celsius Temperature
        ## User validation to prevent number input under absolute zero
        while temp < -459.67:
            print("\n")
            print("Error: Temperature Below Absolute Zero. Please Try Again")
            temp = float(input("Please Enter a Temperature in Fahrenheit: "))
        ## Calls conversion function
        newTemp = to_cels(temp)
        print("\n")
        ## Prints output
        print(f"The Temperature in Celsius is {newTemp:.2f}")

    ## Redisplays menu so user can use another calculator
    menuReturn = menu()

## If user chooses to terminate the program, then the code ends
if menuReturn == 3:
    print("\n")
    print("Thank You For Using My Calculator. Have a Good Day")

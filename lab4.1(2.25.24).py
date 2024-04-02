#### Decision Making Lab 3: Pt 1

### Cost
total_cost = 0

## Intro
print("Welcome to My Pizza Store :D")
print("\n")
print(" Delivery: Enter 1", "\n", "Pickup: Enter 2") # Determines whether to addd
print("\n")

### Aquirement Method
how_to_get = input("Delivery or Pickup? ")

# Checks that the user enters the correct code
while how_to_get != "1" and how_to_get != "2":
    print("\n")
    print("Please Reload and Enter the Correct Code!")
    how_to_get = input("Delivery or Pickup? ")
address = 0

## Gets Address if Uder Wants Delivery
if how_to_get == "1":
    total_cost += 5
    address = input("Please enter delivery address: ")

print("Choose Your Order!")
print("\n")
print("Menu")
print(" Cheese Pizza: Enter 3", "\n", "Garden Fresh Pizza: Enter 4", "\n", "Meat Lovers Pizza: Enter 5")
    
# Get input from user
print("\n")
order = input("Enter Your Pizza Number: ") # Gets the type of pizza the customer wants
order = int(order)
order_name = " " # Used to print the pizza order later

## Automates code only if user enters the correct code
while order < 3 or order > 5:
    print("\n")
    print("Please Enter A Correct Number!")
    order = input("Enter Your Pizza Number: ")
    order = int(order)

## Determine the final cost

if order == 3:
    total_cost += (17.10 + (17.10*0.06))
    order_name = "You've ordered a Cheeze Pizza!"
elif order == 4:
    total_cost += (18.49 + (18.49*0.06))
    order_name = "You've ordered a Garden Fresh Pizza!"
elif order == 5:
    total_cost += (19.75 + (19.75 * 0.06))
    order_name = "You've ordered a Meat Lover's Pizza!"

### Tip
print("\n")
tip = input("Would you like to tip? $")
tip = int(tip) # Turns the float variable into a number
total_cost += tip

## Print final Receipt
print("\n")
print(order_name)
print(f"Your Total is: ${total_cost:.2f}")
if how_to_get == "1":
    print(f"Your Delivery Address is: {address}")

## Final Ending
print("\n")
print("Thank You For Ordering!")

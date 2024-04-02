#### Decision Making Lab 3: Pt 1

## Intro
print("Welcome to My Pizza Store :D")
print("Choose Your Order!")
print("\n")
print("Menu")
print(" Cheese Pizza: Enter 1", "\n", "Garden Fresh Pizza: Enter 2", "\n", "Meat Lovers Pizza: Enter 3")

## Get input from user
print("\n")
order = input("Enter Your Pizza Number: ") # Gets the type of pizza the customer wants
order_name = 0 # Used to print the pizza order later
print("\n")
print(" Delivery: Enter 4", "\n", "Pickup: Enter 5") # Determines whether to add delivery cost or not

### Cost
total_cost = 0

### Aquirement Method
how_to_get = input("Delivery or Pickup? ")
address = 0
if how_to_get == "4":
    total_cost += 5
    address = input("Please enter delivery address: ")
    

### Tip
tip = input("Would you like to tip? $")
tip = float(tip) # Turns the float variable into a number


## Determine the final cost

if order == "1":
    total_cost += (17.10 + (17.10*0.06))
    order_name = "You've ordered a Cheeze Pizza!"
elif order == "2":
    total_cost += (18.49 + (18.49*0.06))
    order_name = "You've ordered a Garden Fresh Pizza!"
elif order == "3":
    total_cost += (19.75 + (19.75 * 0.06))
    order_name = "You've ordered a Meat Lover's Pizza!"
else:
    order_name = "Incorrect code. Please refresh and try again! :/"

## Print final Receipt
print("\n")
print(order_name)
print(f"Your Total is: ${total_cost:.2f}")
if how_to_get == "4":
    print(f"Your Delivery Address is: {address}")

## Final Ending
print("\n")
print("Thank You For Ordering!")

    
    





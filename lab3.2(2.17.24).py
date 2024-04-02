## Ice Cream Store

## Gather User Request
print("Welcome To The Quad Ice Cream Store!")
print("\n")

scoops = input("Number of Scoops : ") # Gets the number of scoops wanted
waffle = input("Do You Want a Waffle Cone? y/n: ") # If they want a waffle cone
if waffle == "y" or waffle == "Y":
    print("Waffle Cone Price is $1.55")

## Convert to Float and Define Additional Variables
scoops = int(scoops)
cost = 0 # Final Cost
scoop_cost = 0 # Defines the cost of each scoop

## Determine Scoop Cost
if scoops < 3:
    scoop_cost = 2.75
else:
    scoop_cost = 2.10 ## Scoop Cost is Less When There Are More Than 2 Scoops

## Calculate Final Cost
cost = (scoop_cost * scoops)
if waffle == "y" or waffle == "Y":
    cost += 1.55 ## Adds Waffle Cost

## Print Final Reciept
print("\n")
print(f"Your Price Per Scoop Is: ${scoop_cost:.2f}")
print(f"You Ordered {scoops} scoops")
print(f"Your Total Cost Is: ${cost:.2f}")
print("Thank You For Buying")

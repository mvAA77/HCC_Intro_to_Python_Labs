temp = input("Please Enter The Celsius Temperature: ")
temp = float(temp)
cTemp = temp
finalTemp = temp + 30
finalTemp = float(finalTemp)
fTemp = 0
kTemp = 0

## Prevents Users From Entering Input Under Absolute Zero
while temp < -273.15:
    print("Error: Under Absolute Zero")
    temp = input("Please Enter The Celsius Temperature: ")
    temp = float(temp)

## Displays Conversion Chart Using While Loop
print("\n")
print("Conversion Chart Using While Loop")
print("\n")
print("     Cels     Fahr     Kelvin")

while temp <= finalTemp:
    fTemp = (9/5) * temp + 32
    kTemp = temp + 275.15
    print(f"{temp:10.2f}{fTemp:10.2f}{kTemp:10.2f}")
    temp += 1

## Displays Conversion Chart Using For Loop
print("\n")
print("Conversion Chart Using For Loop")
print("\n")
print("     Cels     Fahr     Kelvin")


for i in range(0, 30, 1):
    fTemp = (9/5) * cTemp + 32
    kTemp = cTemp + 275.15
    print(f"{cTemp:10.2f}{fTemp:10.2f}{kTemp:10.2f}")
    cTemp += 1

print("Thank You For Using Your Program")

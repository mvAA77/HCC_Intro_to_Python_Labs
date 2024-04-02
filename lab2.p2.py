### Cell Phone Reciept Printer

## Gather User Input

phone_model = input("Enter Your Phone Model: ") # Get Phone Model
phone_cost = input("Enter Your Phone Cost: $") # Get Phone Cost
warranty_cost = input("Enter Your Phone's Warrenty Cost: $") # Get Warrenty Cost

## Turn Numerical Strings Into Float Numbers
phone_cost = float(phone_cost)
warranty_cost = float(warranty_cost)

## Calculate Additional Costs
sales_tax = ((phone_cost + warranty_cost) * 0.05) # Sales Tax: 5% 
shipping_cost = (phone_cost * 0.018) # Shipping Cost: 1.8% of Phone cost

## Calculate Total Cost
total_cost = (phone_cost + warranty_cost + sales_tax + shipping_cost)

## Display Everything
print("\n")
print(" Receipt")
print(f" Model: {phone_model}")
print(f" Phone Cost: ${phone_cost:.2f}")
print(f" Warranty Cost: ${warranty_cost:.2f}")
print(f" Sales Tax: ${sales_tax:.2f}")
print(f" Shipping Cost: ${shipping_cost:.2f}")
print(f" Total Cost: ${total_cost:.2f}")

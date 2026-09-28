# Simple Bill Calculator

# 1. Ask the user for the price of one item and the quantity
item_price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

# 2. Calculate the total cost
total_cost = item_price * quantity

# 3. Print a friendly summary using an f-string
print(f"\n{quantity} items at {item_price:.2f} each = {total_cost:.2f}")
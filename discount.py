#Discount calculator function
def calculate_discount(price, discount_percentage):
	if discount_percentage >= 20:
		discount_amount = price * (discount_percentage / 100)
		discounted_price = price - discount_amount
		return discounted_price
	else:
		return price

#Taking user input
price = float(input("Enter the original price of the item:"))
discount_percentage = float(input("Enter the percentage:"))

discounted_price = calculate_discount(price, discount_percentage)

if discounted_price == price:
	print(f"No discount applied, the price is {price}")
else:
	print(f"Final price after {discount_percentage} percent discount is:  {discounted_price}")
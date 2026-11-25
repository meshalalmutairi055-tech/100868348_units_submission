# Place your answer to Exercise_04 in this file
# Do not rename or remove this file

price_per_copy = 99

num_copies = int(input("Please enter the number of copies of the software you wish to purchase:\n"))

# work out the discount percentage
if num_copies >= 100:
  discount = 50
elif num_copies >= 50:
  discount = 40
elif num_copies >= 20:
  discount = 30
elif num_copies >= 10:
  discount = 20
elif num_copies >= 5:
  discount = 10
else:
  discount = 0

# the calculations are the same whatever the discount is
total_price = num_copies * price_per_copy
discount_amount = total_price * discount / 100
final_price = total_price - discount_amount

if discount > 0:
  print(f"You have been given a {discount}% discount on the normal price of £{price_per_copy}.")

print(f"The total cost is £{final_price:.2f}.")
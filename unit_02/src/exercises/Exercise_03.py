# Place your answer to Exercise_03 in this file
# Do not rename or remove this file
# get the number of each ticket from the user
child_tickets = int(input("How many child tickets would you like?\n"))
adult_tickets = int(input("How many adult tickets would you like?\n"))
senior_tickets = int(input("How many senior tickets would you like?\n"))

# compute the total price
total_price = (child_tickets * 5) + (adult_tickets * 10) + (senior_tickets * 8)

print(f"Total Price: £{total_price}")
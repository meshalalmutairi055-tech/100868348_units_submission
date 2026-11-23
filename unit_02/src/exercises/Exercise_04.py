# Place your answer to Exercise_04 in this file
# Do not rename or remove this file

first_name = input("Please enter your first name:\n")
middle_name = input("Please enter your middle name:\n")
last_name = input("Please enter your last name:\n")

# first character of each name
first_initial = first_name[0].upper()
middle_initial = middle_name[0].upper()
last_initial = last_name[0].upper()

print(f"Hi, your initials are {first_initial}.{middle_initial}.{last_initial}")
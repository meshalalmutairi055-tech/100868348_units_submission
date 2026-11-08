# Place your answer to Lesson_07 in this file
# Do not rename or remove this file

# DO NOT EDIT THESE TWO LINES
firstname = input("Please enter a first name: \n")  # leave this alone!
surname = input("Please enter a surname: \n")  # leave this alone!

# -------------------------------------------------------

# first character of the first name
print(f"The first character of the first name is {firstname[0]}")

# last character of the surname (negative indexing)
print(f"The last character of the surname is {surname[-1]}")

# initials of the person
print(f"The person's initials are {firstname[0]}.{surname[0]}")

# first 3 characters of the first name
print(f"The first 3 characters of the first name are {firstname[:3]}")

# last 4 characters of the surname
print(f"The last 4 characters of the surname are {surname[-4:]}")
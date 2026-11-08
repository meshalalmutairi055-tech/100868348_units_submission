# Place your answer to Exercise_05 in this file
# Do not rename or remove this file


# get the length and height of the wall in metres
length = float(input("Please enter the length of the wall:\n"))
height = float(input("Please enter the height of the wall:\n"))

cans = length * height / 20

cans = int(cans) + (cans % 1 > 0)

print(f"You require {cans} cans of paint.")
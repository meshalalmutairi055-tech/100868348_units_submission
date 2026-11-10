# Place your answer to Exercise_03 in this file
# Do not rename or remove this file

print("This program calculates the largest number from a series of numbers entered.")

# None means no number has been entered yet
largest = None

program_over = False

while not program_over:
  num = int(input("Please enter a number. Enter 0 to stop\n"))
  if num == 0:
    program_over = True
  else:
    # the first number entered is the largest so far
    if largest is None:
      largest = num
    elif num > largest:
      largest = num

if largest is None:
  print("No numbers entered.")
else:
  print(f"The largest of the numbers entered is {largest}")
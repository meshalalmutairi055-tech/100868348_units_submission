# Place your answer to Exercise_01 in this file
# Do not rename or remove this file

print("This program calculates the average of a series of numbers entered.")

# total of the numbers entered so far and how many numbers there have been
total = 0
count = 0

program_over = False

while not program_over:
  num = float(input("Please enter a number. Enter 0 to stop\n"))
  if num == 0:
    program_over = True
  else:
    total += num
    count += 1

if count == 0:
  print("No numbers entered.")
else:
  average = total / count
  print(f"The average of the numbers entered is {average}")
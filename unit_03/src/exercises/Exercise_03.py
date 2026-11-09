# Place your answer to Exercise_03 in this file
# Do not rename or remove this file

choice = int(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:\n"))

if choice == 1:
  celsius = float(input("Please enter the temperature in Celsius:\n"))
  if celsius >= 0:
    fahrenheit = (9/5) * celsius + 32
    fahrenheit = round(fahrenheit, 2)
    print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit.")
  else:
    print("ERROR: You must enter a value of 0 or greater.")
elif choice == 2:
  fahrenheit = float(input("Please enter the temperature in Fahrenheit:\n"))
  if fahrenheit >= 0:
    celsius = (5/9) * (fahrenheit - 32)
    celsius = round(celsius, 2)
    print(f"{fahrenheit} Fahrenheit is equivalent to {celsius} Celsius.")
  else:
    print("ERROR: You must enter a value of 0 or greater.")
else:
  print("ERROR: Invalid option")
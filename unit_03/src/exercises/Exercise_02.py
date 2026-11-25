# Place your answer to Exercise_02 in this file
# Do not rename or remove this file

celsius = float(input("Please enter the temperature in Celsius:\n"))

if celsius >= 0:
  fahrenheit = (9/5) * celsius + 32
  fahrenheit = round(fahrenheit, 2)
  print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit.")
else:
  print("ERROR: You must enter a value of 0 or greater.")
# Place your answer to Exercise_01 in this file
# Do not rename or remove this file

celsius = float(input("Please enter the temperature in Celsius:\n"))

# only calculate and display the result if the temperature is not negative
if celsius >= 0:
  fahrenheit = (9/5) * celsius + 32
  fahrenheit = round(fahrenheit, 2)
  print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit.")
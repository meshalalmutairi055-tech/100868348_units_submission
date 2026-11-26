
# Place your answer to Exercise_02 in this file
# Do not rename or remove this file

speed = int(input("What is the speed of the vehicle in mph?\n"))
hours = int(input("\nHow many hours has it travelled?\n"))
print()

if speed <= 0:
  print("ERROR: Speed must be a positive number.")
elif hours <= 0:
  print("ERROR: Hours travelled must be a positive number.")
else:
  print("Hour | Distance Travelled")
  print("-----------------------")
  for hour in range(1, hours + 1):
    distance = speed * hour
    print(f"{hour}    | {distance}")
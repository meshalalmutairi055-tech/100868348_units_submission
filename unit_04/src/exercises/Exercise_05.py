# Place your answer to Exercise_05 in this file
# Do not rename or remove this file

# The Number Guessing Game 
import random

# randomly generate a number between 1 and 10
#secret_guess = random.randint(1,10)
secret_guess = 3

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")
print("\nIf you wish to exit the game enter 0...\n")

guess = int(input("Please enter a guess:\n"))
number_of_guesses = 1

while (guess != secret_guess) and (guess != 0):
  if guess > secret_guess:
    print("Your guess is too high, please try again.")
  else:
    print("Your guess is too low, please try again.")
  guess = int(input("Please enter a guess:\n"))
  number_of_guesses += 1

if guess == 0:
  print(f"Program exited. The correct answer was {secret_guess}")
else:
  print(f"Well done the correct answer was {secret_guess}")
  print(f"You took {number_of_guesses} guesses.")
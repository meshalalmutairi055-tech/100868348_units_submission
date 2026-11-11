def num_digits(n):
    digits = 0
    # divide by 10 until the number is less than 1, counting the divisions
    while n >= 1:
        n = n / 10
        digits += 1
    return digits

def main():
    try:
        number = int(input("Please enter a positive whole number:\n"))
        if number > 0:
            digits = num_digits(number)
            if digits == 1:
                print(f"{number} has {digits} digit.")
            else:
                print(f"{number} has {digits} digits.")
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")

# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":
    main() # calls the main function
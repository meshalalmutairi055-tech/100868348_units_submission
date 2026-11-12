def main():
    numbers = []
    program_over = False

    while not program_over:
        user_input = input("Please enter the next number: ")
        if user_input == "q":
            program_over = True
        else:
            numbers.append(int(user_input))
            # stop once 10 numbers
            if len(numbers) == 10:
                program_over = True

    if len(numbers) == 0:
        print("No numbers entered.")
    else:
        print("The reverse of the numbers entered is:")
        
        for i in range(len(numbers) - 1, -1, -1):
            print(numbers[i])

# This is the entry point of the program
if __name__ == "__main__":
    main()  # call the main function
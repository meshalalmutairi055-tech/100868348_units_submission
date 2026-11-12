import random

def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list

def main():
    rand_num_list = rand_num_list_gen()
    print("I have generated 100 random numbers between 1 and 50.")
    print("The count in the following ranges is:")

    # one counter for each range
    count_1_10 = 0
    count_11_20 = 0
    count_21_30 = 0
    count_31_40 = 0
    count_41_50 = 0

    for number in rand_num_list:
        if number <= 10:
            count_1_10 += 1
        elif number <= 20:
            count_11_20 += 1
        elif number <= 30:
            count_21_30 += 1
        elif number <= 40:
            count_31_40 += 1
        else:
            count_41_50 += 1

    print(f"1..10: {count_1_10}")
    print(f"11..20: {count_11_20}")
    print(f"21..30: {count_21_30}")
    print(f"31..40: {count_31_40}")
    print(f"41..50: {count_41_50}")

def advanced_main():
    num_to_gen = input(
        "Please enter the number of integers to generate from the range:\n\n"
    )
    ranges = input(
        "Please enter the ranges in the following format 1..5,6..10,11..20\n\n"
    )
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))

    print("The count in the given ranges is:\n")
    range_list = ranges.split(",")

    for range_text in range_list:
       
        bounds = range_text.split("..")
        lower = int(bounds[0])
        upper = int(bounds[1])

        
        count = 0
        for number in rand_num_list:
            if lower <= number <= upper:
                count += 1

        print(f"{range_text}: {count}")

if __name__ == "__main__":
    main()
    # advanced_main()
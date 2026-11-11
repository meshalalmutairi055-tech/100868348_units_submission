def print_list(input_list, multiple=1):
    # print each item multiplied by multiple (1 by default)
    for item in input_list:
        print(item * multiple)

if __name__ == "__main__":
    print_list([4,1,6,7], multiple = 2)
    print_list([4,1,6,7], multiple = 3)
    print_list([4,1,6,7])
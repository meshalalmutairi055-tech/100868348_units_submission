def find_max_row(grid):
    # HINT: https://datagy.io/python-index-of-max-item-list/
    max_sum = None
    max_row = 0
    row_number = 1
    for row in grid:
        # add up the items in this row
        row_sum = 0
        for item in row:
            row_sum += item

        
        if max_sum is None or row_sum > max_sum:
            max_sum = row_sum
            max_row = row_number

        row_number += 1

    return max_row

    

def print_grid(grid):
    for row in grid:
        print(row)

if __name__ == "__main__":
    # main
    grid_one = [[1, 2, 3], [4, 2, 1], [4, 5, 4]]
    print_grid(grid_one)
    print(
        f"The maximum row for the grid_one is {find_max_row(grid_one)}"
    )  # should return 3

    print()

    grid_two = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
    print_grid(grid_two)
    print(
        f"The maximum row for the grid_two is {find_max_row(grid_two)}"
    )  # should return 1

    print()

    grid_three = [[1, 2, 3], [3], [2, 1, 3, 4]]
    print_grid(grid_three)
    print(
        f"The maximum row for the grid_three is {find_max_row(grid_three)}"
    )  # should return 3
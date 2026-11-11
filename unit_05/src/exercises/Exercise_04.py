def arithmetic_sum(a, d, n):
    total = 0
    term = a
    # add each term to the total, then move to the next term
    for i in range(n):
        total += term
        term += d
    return total

if __name__ == "__main__":
    print(arithmetic_sum(1,1,100))   # prints the return value - 5050
    print(arithmetic_sum(3,2,15))    # prints the return value -  255
    print(arithmetic_sum(10,4,5))    # prints the return value -  90
    print(arithmetic_sum(-5, -2, 20))    # prints the return value -  -480
def calc_change(change):
    # returns a list with the number coins
    coins = [50, 20, 10, 5, 2, 1]
    coin_counts = []

    for coin in coins:
        # how many of this coin
        coin_counts.append(change // coin)
        
        change = change % coin

    return coin_counts

def main():
    amount = int(input("Please enter the amount inserted (1 to 100):\n"))

    if amount < 1 or amount > 100:
        print("Invalid amount")
    else:
        cost = int(input("Please enter the cost of the item:\n"))

        if cost > amount:
            print("Item costs more than amount inserted")
        else:
            coin_counts = calc_change(amount - cost)
            print(f"Number of 50p coins is {coin_counts[0]}")
            print(f"Number of 20p coins is {coin_counts[1]}")
            print(f"Number of 10p coins is {coin_counts[2]}")
            print(f"Number of 5p coins is {coin_counts[3]}")
            print(f"Number of 2p coins is {coin_counts[4]}")
            print(f"Number of 1p coins is {coin_counts[5]}")

if __name__ == "__main__":
    main()
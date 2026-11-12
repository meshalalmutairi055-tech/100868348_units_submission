def change_list(my_list):
    
    new_list = my_list.copy()
    # remove the second item
    new_list.pop(1)
    new_list.append("Banana")
    new_list.sort()
    return new_list

if __name__ == "__main__":
    fruit_list = ["Pear", "Orange", "Peach", "Apple"]
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    new_fruit_list = change_list(fruit_list)
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]
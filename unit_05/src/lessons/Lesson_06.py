import copy

def update_list_item_one(items, x):
  # change the first item 
  items[0] = x

def new_list_item_one(items, x):
  # create a copy
  new_list = copy.copy(items)
  new_list[0] = x
  return new_list

if __name__ == "__main__":
    list_one = [1,2,3,4]
    update_list_item_one(list_one, 0)
    print(list_one) # should print out [0,2,3,4]
    
    list_one = [1,2,3,4]
    new_list_item_one(list_one, 0)
    print(list_one) # should print out [1,2,3,4]
    
    list_one = [1,2,3,4]
    list_one = new_list_item_one(list_one, 0) # bind the new object to l
    print(list_one) # should print out [0,2,3,4]
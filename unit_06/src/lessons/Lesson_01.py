def longest_word(string_list):
    longest = None

    for word_list in string_list:
        for word in word_list:
            
            if longest is None or len(word) > len(longest):
                longest = word
        return longest
  
def num_characters(string_list):
    total = 0

    for word_list in string_list:
        for word in word_list:
            total += len(word)

    return total
  
if __name__ == "__main__":
    test_string = [["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]
    test_string2 = [["Hello", "World"], ["Apple", "Pears"]]
    print(longest_word(test_string)) # should print revolution
    print(num_characters(test_string)) # should print 105
    print(longest_word(test_string2)) # should print hello
    print(num_characters(test_string2)) # should print 20
# Place your answer to Lesson_03 in this file
# Do not rename or remove this file

# Do not touch this line - It is just there to set up the string list from the input
# string_list will contain a list of strings that have been entered.
string_list = input("Please enter a list of numbers separated by a comma.\ne.g. Citreon,Ford,Audi,Mercedes\n").split(',')

for word in string_list:
  print(f"The length of the string {word} is {len(word)}.")
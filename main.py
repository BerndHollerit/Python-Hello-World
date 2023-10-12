import python_file_to_import

print("Hello World")

print (1 + 2)

string_one = "String"
string_two = "concatenation"

print(string_one + " " + string_two)

my_string = "This is a string!"
print(my_string)
print(my_string.upper())
print(my_string.lower())

# prints all the string methods
print(dir(my_string))

# Shows help of capitalize method
help(my_string.capitalize)

my_string = "I like Python!"
print(my_string)
# Prints first character of string
print(my_string[0:1])

print(my_string[2:])
print(my_string[0:-5])
print(my_string[4:10])

# User input
# name = input("Enter your name: ")
# print("Hello", name + "!")

python_file_to_import.display_message()
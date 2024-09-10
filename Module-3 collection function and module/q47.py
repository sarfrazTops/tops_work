#(47)Write a Python program to create a dictionary from a string.


string = "w3resource"


dict = {}


for char in string:
    if char in dict:
        dict[char] += 1  # Increment the count if character is already in dictionary
    else:
        dict[char] = 1   # Add character to dictionary with count 1

print(dict)


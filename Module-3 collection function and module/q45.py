#(45)  Write a Python program to find the highest 3 values in a dictionary.
# 
dict = {
    'a': 50,
    'b': 15,
    'c': 89,
    'd': 20,
    'e': 95,
    'f': 65
}
highest_values = sorted(dict.values(), reverse=True)[:3]
print("The highest 3 values are:", highest_values)

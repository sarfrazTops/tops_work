#(19)Write a Python program to create a tuple with different data types.

mix_tuple = (1, "hello", 3.14, True, [1, 2, 3], {"key": "value"}, (7, 8, 9))
print("Tuple:", mix_tuple)
for item in mix_tuple:
    print(f"Element: {item}, Type: {type(item)}")

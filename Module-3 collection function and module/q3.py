#(3)Differentiate between append () and extend () methods?

#1. append() Method
#Adds a single element (of any data type) to the end of the list.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#2.extend()
# Adds each element of an iterable (like a list, tuple, or string) to the end
#of the list.

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  

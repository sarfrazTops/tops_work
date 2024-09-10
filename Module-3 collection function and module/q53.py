#(53)How can you pick a random item from a list or tuple? 

#In Python, you can use the random module to pick a random item from a list or tuple.
#Specifically, the function random.choice() is used to select a random item.

import random

list = [1, 2, 3, 4, 5]
ran_item = random.choice(list)
print(ran_item)

import random

tup = (1, 2, 3, 4, 5)
ran_item = random.choice(tup)
print(ran_item)

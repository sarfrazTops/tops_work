#(57) How will you randomizes the items of a list in place? 

#The method shuffle() can be used to randomize the items of a list in place.
#It should be noted that this function is not accessible directly and therefore
#we need to import or call this function using random static object.
#Here, 'lst' is passed as a parameter which could be a list or tuple.

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


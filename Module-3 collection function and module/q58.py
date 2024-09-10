#(58)Write a Python program to read a random line from a file.

import random

fd=open(r"C:\Users\sarfr\Desktop\pro")
lines=fd.readlines()
print(random.choice(lines))
fd.close


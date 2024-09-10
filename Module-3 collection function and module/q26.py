#(26)Q.26 write a python program to replace last value of tuples in a list.

l=[(10,20,30,50),(50,60,70),(70,80,90)]
print([t[:-1]+(100,)for t in l])



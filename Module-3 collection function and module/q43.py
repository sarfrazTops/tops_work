#(43)Why Do You Use the Zip () Method in Python? 

#The zip() method in Python is used to combine two or more iterables.
#(such as lists, tuples, or strings) element by element into tuples

lis_1=[11,22,33,44]
lis_2=[10,20,30,40]
for a,b in zip(lis_1,lis_2):
    print(a,b)

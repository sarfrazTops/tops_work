#(2)How will you remove last object from a list?
#Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]

#first method
list1 = [2, 33, 222, 14, 25]
list1.pop()  
print(list1)


#second method
list1 = [2, 33, 222, 14, 25]
del list1[-1]  
print(list1)  

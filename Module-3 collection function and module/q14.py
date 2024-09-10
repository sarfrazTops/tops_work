#(14)Write a Python program to find the second smallest number in a list. 


#ans:-
n=int(input("Enter the total no of element you want inside your list: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print("My list",l)
sorted_list=l.sort()
print("sorted: ",l)
second_smallest=l[-2]
print("second samallest element",second_smallest)

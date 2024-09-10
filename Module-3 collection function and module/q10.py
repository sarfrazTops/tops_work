#Q.10 write a python program to generate  and print a list of first and last 5 elements where the values are square of numbers
#between 1 and 30.

#ans:-
squar=[i**2 for i in range(1,31)]
first_five=squar[:5]
last_five=squar[-5:]
print("first 5 elements:",first_five)
print("last 5 elements:",last_five)


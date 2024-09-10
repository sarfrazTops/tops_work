#Q.28 write a python program to remove an empty tuple(s) from a list of a tuple.

List=[(),(),('',),('a','b'),('a','b','c'),('d')]
List=[t for t in List if t]
print(List)

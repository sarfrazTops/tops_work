#Q.6 write a python program to count the program of strings where the string length is 2
#or more and the first and last character are same from a given list of strings.

#ans:-
s=0
list1=['aba',124,'kgf','gfd']
for x in list1:
    if len(x)>1 and x [0]==x[-1]:
        print(x)
        s=s+1
        print(s)



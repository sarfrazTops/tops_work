#(48)Write a Python function to calculate the factorial of a number (anonnegative integer). 

def fact(num):
    fact=1
    if num<0:
        print("factorial does not exit for negative number")
    elif num==0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fact = fact * i
        print("The factorial of",num,"is",fact)
n=int(input("Enter the number "))
fact(n)

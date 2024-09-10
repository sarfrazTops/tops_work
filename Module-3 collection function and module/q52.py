#(52)How Many Basic Types Of Functions Are Available In Python?

#There are two types of functions in python: User-Defined Functions - these types of functions 
#are defined by the user to perform any specific task. 
#Built-in Functions - These are pre-defined functions in python.

#1. Built-in Functions
#These are functions that are provided by Python itself, and you can use them directly without
#needing to define them.
#Example: print(), len(), sum(), type(), etc.

#2. User-defined Functions
#These are functions that you create to perform specific tasks. 
#You define them using the def keyword.

#Example:-
def my_function():
    print("Hello, World!")

#(3). Lambda Functions (Anonymous Functions)
#These are small, anonymous functions that are defined using the lambda keyword. 
# They can have any number of arguments but only one expression.

square = lambda x: x * x
print(square(5))  # Output: 25

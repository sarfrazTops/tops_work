#(63)Write a Python program to returns sum of all divisors of a number.

num = int(input("Enter a number: "))

i= 0
for i in range(1, num + 1):
    if num % i == 0:  
        i += i

print(f"The sum of all divisors of {num} is {i}")

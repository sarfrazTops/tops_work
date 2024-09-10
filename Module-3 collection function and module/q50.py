#(50)Write a Python function to check whether a number is perfect or not.

def per_num(num):
    if num < 1:
        return False
    
    divisors_sum = 0
    
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
   
    return divisors_sum == num

number = 6
if per_num(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

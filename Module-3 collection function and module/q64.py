#(64)Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 

deci_num = [23.45, 67.89, 12.34, 98.76, 45.67]


max = deci_num[0]
min = deci_num[0]


for number in deci_num:
    if number > max:
        max = number
    if number < min:
        min = number

print("Maximum number",(max))
print("Minimum number",(min))

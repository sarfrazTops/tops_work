#(62)Write a Python program to calculate surface volume and area of a cylinder.
# 
pi=22/7

height=float(input("Height oh cylinder is: "))
radius=float(input("Radius oh cylinder is: "))

volume=pi *radius*radius*height
surface=((2*pi*radius)*height)+((pi*radius**2)*2)
print("The volume of the cylinder is: ",(volume))
print("The surface of the cylinder is:",(surface)) 

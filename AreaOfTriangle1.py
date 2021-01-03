# Python program to calculate the area of a triangle using half-perimeter

# take input from users for 3 sides of triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# calculating the half-perimeter
s = (a + b + c)/2

# calculating the area of triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of triangle is {}".format(area))
# python program to find out the quadratic equation a*x**2 + b*x + c = 0

# import complex math module
import cmath

# a = 1, b = 5, c = 6
# take 3 input from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# calculate the discremenant
d = b*b - 4*a*c

# find two root
root1 = (-b - cmath.sqrt(d))/(2*a)
root2 = (-b + cmath.sqrt(d))/(2*a)

# print roots of equation
print("{} and {} are the roots of equation".format(root1, root2))
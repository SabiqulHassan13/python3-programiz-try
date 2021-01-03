# python program to find out sqrt of a complex number

# import the complex math module
import cmath

# take a number input from the user
num = eval(input("Enter a complex number: "))

# finding sqrt of num
numSqrt = cmath.sqrt(num)

# display the sqrt of num
print("The Square root of {0} is {1:0.2f}+{2:0.2f}j".format(num, numSqrt.real, numSqrt.imag))
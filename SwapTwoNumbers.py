# Python program to swap two numbers

# Take input two numbers from user
a = input("Enter first number: ")
b = input("Enter second number: ")

# swap two numbers using temporary variable
temp = a
a = b
b = temp

# display two numbers after swap
print("After swapping first number is {}".format(a))
print("After swapping second number is {}".format(b))

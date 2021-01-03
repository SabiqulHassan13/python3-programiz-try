# python program to find out the largest number among three

# take a number input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# decision making
if (num1 > num2) and (num1 > num3):
    largest = num1
    print("{} is the largest number".format(largest))
elif (num2 > num1) and (num2 > num3):
    largest = num2
    print("{} is the largest number".format(largest))
else:
    largest = num3
    print("{} is the largest number".format(largest))
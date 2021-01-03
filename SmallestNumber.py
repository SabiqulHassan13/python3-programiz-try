# python program to find the smallest number among 3 numbers

# take 3 numbers input from user
num1 = float(input("Enter 1 number: "))
num2 = float(input("Enter 2 number: "))
num3 = float(input("Enter 3 number: "))

# find the smallest one
if (num1 < num2) and (num1 < num3):
    print("{} is the smallest number".format(num1))
elif (num2 < num1) and (num2 < num3):
    print("{} is the smallest number".format(num2))
else:
    print("{} is the smallest number".format(num3))
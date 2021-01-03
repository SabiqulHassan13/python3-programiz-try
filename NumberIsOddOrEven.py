# python program to check a number is even or odd

#take input a number to check from the user
num = float(input("Enter a number: "))

# checking a number is odd or even
if num % 2 == 0:
    print("{} is even number".format(num))
elif num % 2 == 1:
    print("{} is odd number".format(num))
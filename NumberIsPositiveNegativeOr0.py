#python program to check if a number is positive, negative or 0

# take a number input for check
num = float(input("Enter a number: "))

# checking condition
if num > 0 :
    print("{} is a positve number".format(num))
elif num < 0 :
    print("{} is a negative number".format(num))
elif num == 0 :
    print("{} is a zero".format(num))
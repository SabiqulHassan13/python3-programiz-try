# python program to check a number is prime or not

# take a number input to check
num = int(input("Enter a number: "))

# prime number is greater than 1
if num > 1:
    # check for factors
    for i in range(2,num):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            break;
    else:
        print("{} is a prime number".format(num))

# if input number is less than or equal to 1 it will not be prime number
else:
    print("{} is not a prime number".format(num))

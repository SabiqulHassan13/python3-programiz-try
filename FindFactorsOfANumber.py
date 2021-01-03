# python program to find the factors of a number

# take input a number
num = int(input("Enter a positive integer: "))

# print the factors
print("The factors of {} are: ".format(num))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

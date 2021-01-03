# python program to check a year is leap year or not

# take input a number
year = int(input("Enter a year: "))

# checking lea0 year
if year % 400 == 0:
    print("{} is a leap year".format(year))
elif year % 4 == 0:
    if year % 100 != 0:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))

# Arup Guha
# 5/31/2012
# A second method to determine if a year is a leap year or not.

def main():

    # Get the year from the user.
    year = int(input("Please enter a year.\n"))

    # Assume we don't have a leap year.
    result = False

    # Usually, if it's divisible by 4, it's a leap year.
    if year%4 == 0:
        result = True

    # Go back and fix our result for the weird years (1700, 1800, 1900, etc.)
    if year%100 == 0 and year%400 != 0:
        result = False

    # Print the end result.
    if result:
        print(year,"was a leap year.")
    else:
        print(year,"was not a leap year.")

main()

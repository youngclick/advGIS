# Arup Guha
# 3/9/2013
# Simplified Tax Code to illustrate if statement

# Note: These are not the actual values, but they are relatively close.
SINGLE_DEDUCTION = 5000
MARRIED_DEDUCTION = 9000

# Here we implement a graduated income tax with two tax brackets. Our system
# in the US has several more brackets. The idea is as follows:

# For this specific example, all of your taxable income up to 40000 is taxed
# at 15%, while any excess taxable income beyond that value is taxed at 25%.
TAX_BRACKET1 = 15
TAX_BRACKET2 = 25
CUTOFF = 40000

def main():

    # Get user input.
    gross_income = int(input("What is your total yearly income, in dollars?\n"))
    married = input("Are you married(yes/no)?\n")

    # Subtract standard deduction.
    if married == "yes":
        net_income = gross_income - MARRIED_DEDUCTION
    else:
        net_income = gross_income - SINGLE_DEDUCTION

    if net_income < 0:
        tax = 0
    elif net_income < CUTOFF:
        tax = net_income*TAX_BRACKET1
    else:
        tax = CUTOFF*TAX_BRACKET1/100 + (net_income - CUTOFF)*TAX_BRACKET2/100
    
    print("You will pay",tax,"in income taxes this year.")
    print("This is ",tax/gross_income*100,"% of your earnings.", sep="")
    print("After taxes, you will have",gross_income-tax,"dollars left.")

main()

# Arup Guha
# 3/9/2013
# Simplified Tax Code to illustrate if statement

# Note: These are not the actual values, but they are relatively close.
SINGLE_DEDUCTION = 5000
MARRIED_DEDUCTION = 9000

# Pure fiction, but not a bad guess to approximate regular taxes.
TAX_PERC = 17

def main():

    # Get user input.
    gross_income = int(input("What is your total yearly income, in dollars?\n"))
    married = input("Are you married(yes/no)?\n")

    # Subtract standard deduction.
    if married == "yes":
        net_income = gross_income - MARRIED_DEDUCTION
    else:
        net_income = gross_income - SINGLE_DEDUCTION

    tax = net_income*TAX_PERC/100
    print("You will pay",tax,"in income taxes this year.")
    print("This is ",tax/gross_income*100,"% of your earnings.", sep="")
    print("After taxes, you will have",gross_income-tax,"dollars left.")

main()
        

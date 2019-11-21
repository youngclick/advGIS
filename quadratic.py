# Arup Guha
# 3/9/2013
# Quadratic Formula

import math

def main():

    # Get coefficients for equation.
    a = float(input("What is a in your quadratic equation?\n"))
    b = float(input("What is b in your quadratic equation?\n"))
    c = float(input("What is c in your quadratic equation?\n"))

    # Complex case.
    if math.pow(b,2) - 4*a*c < 0:
        print("Sorry your equation has complex roots.")

    # Print out real solutions.
    else:
        disc = math.sqrt(math.pow(b,2) - 4*a*c)
        root1 = (-b + disc)/(2*a)
        root2 = (-b - disc)/(2*a)
        print("Your roots are",root1,"and",root2)

main()
        

def main():
    perc = int(input("What is your percentage in class? \n"))
    if perc >= 90:
        print("You got an A!")
    elif perc >= 80:
        print("You got a B!")
    elif perc >= 70:
        print("You got a C.")
    elif perc >= 60:
        print("You got a D.")
    else:
        print("Sorry, you got a F.")


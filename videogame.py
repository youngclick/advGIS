# Arup Guha
# 3/9/2013
# Buying a Video Game

GAME_COST = 50

def main():

    money = int(input("How much money do you have in dollars?\n"))
    behavior = input("Did you behave well this week(yes/no)?\n")

    # Use of and
    if money >= GAME_COST and behavior == "yes":
        print("Great, you get to buy the game!")

    # Since this is an elif clause, we know if this is true, behavior was bad!
    elif money >= GAME_COST:
        print("Too bad you didn't behave, you would have gotten the game otherwise.")

    # By the same reasoning, we know that they didn't have enough money in this case.
    elif behavior == "yes":
        print("Good behavior! You'll save up the money for the game soon.")

    # Neither option is satisfied.
    else:
        print("Work on your behavior first, then we can think about money.")
main()            

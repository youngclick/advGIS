# Arup Guha
# 10/6/2012

def main():

    ans1 = input("There is a creaky door. Do you open it?\n")

    # For people who want adventure!
    if ans1 == "yes":

        ans2 = input("There is a monster. Do you run?\n")

        if ans2 == "yes":
            print("Great, you are saved!\n")
        else:
            print("Sorry, the monster ate you :(\n")

    # Safe route...
    else:

        ans2 = input("It is hot out here. Do you want ice tea?\n")

        # Get something to drink!
        if ans2 == "yes":
            print("Great, you are energized and refreshed.")
        else:
            print("Sorry, you got heat stroke, and then the monster ate you.")

main()

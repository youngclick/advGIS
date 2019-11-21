# Arup Guha
# 3/9/2013
# Fortune Teller

def main():

    choice = int(input("Choose a number in between 1 and 4, inclusive.\n"))

    # A bit of error checking.
    if not (choice >= 1 and choice <= 4):
        choice = int(input("Sorry, try again, in between 1 and 4.\n"))

    # Print out fortune!
    if choice == 1:
        print("You will win $100000 in the next two years!")
    elif choice == 2:
        print("Your dance team will win its competition!")
    elif choice == 3:
        print("You will go on a game show and have to eat bugs!")
    else:
        print("You will have to work for an ogre!")

main()

        

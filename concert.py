# Arup Guha
# 3/9/2013
# Concert Tickets

def main():

    # Get user input.
    havetix = input("Did you buy concert tickets?\n")
    wontix = input("Did you win concert tickets on the radio?\n")

    # Print out whether they get to go to the concert or not.
    if havetix == "yes" or wontix == "yes":
        print("Great, you get to go to the concert!")
    else:
        print("Looks like you can't go to the concert.")

main()

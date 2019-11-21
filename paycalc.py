# Arup Guha
# 2/16/2013
# Pay Calculator - calculates how much money we made for an hourly job.

payrate = float(input("How much do you get paid an hour?\n"))
hours = int(input("How many hours did you work?\n"))
money = payrate*hours
print("You will make",money,"dollars")

'''
Created on May 25, 2012

@author: Alex Marich
'''

'Declaring tax_Rate and sum'
tax_Rate = .065;
sum = 0;

'''
Assigning the value of variables can be easily defined in Python with one simple
function. The input message is defined as the first parameter in the function.
As soon as the command is processed, the words written in the quotes will be
displayed onto the screen and it automatically seeks the value of what you will
put in.
'''
item_Price = input("What is the price of your first item?\n");
'''
The input function generall takes anything you put into it as a string. So in
order to turn it into a possible number to add sum with, you need to pass it
as a float. A float is basically a number that includes decimal places.
'''
sum += float(item_Price);

'Redefining the value of item_Price with a new input value.'
item_Price = input("What is the price of your second item?\n");
sum += float(item_Price);

'Calculate the final price including tax'
final_Price = sum*(1 + tax_Rate);

'Prints the value to the screen.'
print("The cost of your purchase with tax is " + str(final_Price) + ".")

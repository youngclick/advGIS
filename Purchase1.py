'''
Created on May 25, 2012

@author: Alex Marich
'''

'''
Variables are sets of information within the program that are given a name. 
tax_Rate, shown below, would be the name of the variable, and .065 would be the
value of the variable.

Variables are not given a type, they are defined by what the value of the variable
is set as(i.e. num = 5; -----> num is an integer, num = 5.01; -----> num is a float)
'''
tax_Rate = .065;
'''
Using a ; at the end of a statement is not necessary, if taken out(i.e. num = 5),
the statement will still process correctly and the command will be executed.
'''
item_Price = 8.79;
'''
Math in Python is a lot like math in real life with a few exceptions. In this situation
math is done within the declaration of final_Price. Additionally, it is using the value 
previously defined as item_Price and tax_Rate(values .065 and 8.79 respectively) in 
order to calculate the final price of the item.

Exceptions that differ from normal math that you may use in real life is that when you
are using the order of operations, Python does not allow you to stick a number or 
variable right next to a set of parentheses in order to define multiplication. The 
operator that is being used must be explicitly stated in order to work correctly. 
'''
final_Price = item_Price*(1 + tax_Rate);

'''
There are different predefined functions within the Python library that allow us to
perform certain tasks more quickly and effectively. In this case, we are using the
function print() within the Python library that takes whatever is in the parenthesis
and attempts to print them onto the screen.

Whenever using a function, you must open and close the parentheses( '(' and ')' ) in order to 
fulfill the function requirements. For print() you must have a string of characters
inside of quotation marks or apostrophes(" " or ' ') so you can tell it what to explicitely
say, use + to concatenate(push together) two sets of strings. Python does not concatenate
integers and floats on it's own. You must use another function in order to take the exact
value of the number that you set the variable to and create a string of characters out 
of it. str(), which takes the value of final_Price and creates a sequence of characters
out of them, is used on final_Price so that it may be used with the print function and
be displayed onto the screen.
'''

print("Your purchase costs " + str(final_Price) + " including tax.");







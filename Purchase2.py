'''
Created on May 25, 2012

@author: Alex Marich
'''

tax_Rate = .065;

'''
Python allows you to set multiple variable values on the same line. In this case, 
we are setting both item_Price and sum equal to 0. We do this by seperating the two
variable names with a comma(','), use one equal sign and seperate the values of each 
variable with a comma. The value of the first variable is going to be the value that
you stated first, and the second variables value will be the value that you stated
second.
'''
item_Price, sum = 0, 0;

'''
Variables that defined are capable of being redefined at almost any time you need 
it to change. In this case, we took the original value of item_Price, 0, and 
redeclared the value to be 5.5. 
'''
item_Price = 5.5;
'''
There are different ways we can accomplish adding a number to an already defined
variable. The variable sum was defined as being 0, however we want to take the 
old value of sum and add an extra number on top of it so that the value will 
increase by the number that was specified. You can accomplish this by just 
re-defining the value of sum in a mathematical expression as shown below.
'''
sum = sum + item_Price;

'Giving item_Price a new value'
item_Price = 7.89;
'''
Additionally, you can take the variable sum and add, subtract, multiply, and divide
it by itself by just changing the way the variable defines itself. In order to 
accomplish this you can do:
sum += item_Price;
This will take the value of sum and add the value of item_Price to it and set the
variable sum back to the sum of those two values.
'''
sum += item_Price;

'Find the price of both items including tax'
final_Price = sum*(1 + tax_Rate);

'Print out the purchase with tax'
print("Your purchase cost " + str(final_Price) + " with tax.")
i = 2
while (i < 100):
    j = 2
    while (j <= (i/j)): #7/3=2.xx, 3<=2.5 false, pass
        if not(i%j): # if 7%2 == 1 so pass
            break # break where to go? get out of while loop 
        j = j + 1
    if (j > i/j) : # ok, 2> 6/2==3 so not true get out of if statement.
        print i, " is prime"
    i = i + 1 # define i as variable that 6 + 1 equal 7
print "Good bye!"
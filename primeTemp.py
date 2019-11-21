n = int(raw_input("what number should I go up to? "))

i = 2
while n > i:
    if n % i == 0:
        print "not a prime number"
    i = i + 1
else:
    print "prime number"

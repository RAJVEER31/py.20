def treerec (n, num):
    if n < 1 or n > num:
        return
    print (n)
    treerec (n - 1 , num)
    print (n)
print ("Enter a number:")
num = int (input ())
print ("The numbers from 1 to", num, "and back are:")
treerec(num, num)
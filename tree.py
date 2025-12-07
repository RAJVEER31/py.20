def treerec (num):
    if num < 1:
        return
    treerec (num - 1)
    print (num)
print ("Enter a number:")
num = int (input ())
print ("The numbers from 1 to", num, "are:")
treerec(num)
def tailrec (num, n):
    if n > num:
        return
    print (n)
    tailrec (num, n + 1)
print ("Enter a number:")
num = int (input ())
print ("The numbers from 1 to", num, "are:")
tailrec(num, 1)
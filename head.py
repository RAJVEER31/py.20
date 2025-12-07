def headrec (num, n):
    if n > num:
        return
    headrec (num, n + 1)
    print (n)
print ("Enter a number:")
num = int (input ())
print ("The numbers from 1 to", num, "are:")
headrec(num, 1)
for count in range (0, 1):
    a= int (input("inserire sk 1: "), 16)
    x= 0xFF
    r1= hex ( a^x)

    b= int (input("inserire sk 2: "), 16)
    x= 0xFF
    r2= hex ( b^x)

    c= int (input("inserire sk 3: "), 16)
    x= 0xFF
    r3= hex ( c^x)

    d= int (input("inserire sk 4: "), 16)
    x= 0xFF
    r4= hex ( d^x)

    e= int (input("inserire sk 5: "), 16)
    x= 0xFF
    r5= hex ( e^x)


print ("sk: ", hex(a), hex(b), hex(c), hex(d), hex(e), r5, r4, r3, r2, r1)
USCITA= int (input("premere invio per uscire"), 16)
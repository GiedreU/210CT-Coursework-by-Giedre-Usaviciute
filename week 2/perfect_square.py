
def perfect( n ):
    found = False
    k = 1
    while not found:
        square = k*k
        if square < n:
            k+=1
            continue
        elif square > n:
            print((k-1)**2)
            found = True
        elif square==n:
            print(square)
            found = True
        
perfect(37)
            
        

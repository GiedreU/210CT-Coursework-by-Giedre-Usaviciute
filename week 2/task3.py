def perfect( n ):
    '''function takes a positive integer and return a perfect square which is less or equal to it'''
    found = False
    k = 1
    while not found:
        square = k*k
        if square < n:#increase k until square becomes bigger than given positive int
            k+=1
            continue
        elif square > n:#if square is bigger, return previous square value
            return((k-1)**2)
            found = True
        elif square==n:
            return (square)#if its is equal, return square
            found = True
        
perfSquare = perfect(37)
            
        

def factorial(num):

    if num > 1:                               (n)
        return(num * factorial(num-1))        (n) 
    elif num == 1:                            (1)
        return(num)                           (1)
    
def countZero(n):

    n = [int (i) for i in str(factorial(n))]  (n)
    count = 0                                 (1)
    leng = len(n)                             (1)
    while leng!=0:                            (1)
        if n[leng-1] == 0:                    (n)
            count+=1                          (n)
        leng-=1                               (n)
    return (count)                            (1)
    
Big 0 = O(n)
 

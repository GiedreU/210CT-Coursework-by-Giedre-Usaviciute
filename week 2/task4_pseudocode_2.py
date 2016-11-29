def factorial(num):

    if num > 1:                               #(1)
        return(num * factorial(num-1))        #(n, because its a recursive function which is called n times) 
    elif num == 1:                            #(1)
        return(num)                           #(1)
    
def countZero(n):

    n = [int (i) for i in str(factorial(n))]  #(n, because of FOR loop)
    count = 0                                 #(1)
    leng = len(n)                             #(1)
    while leng!=0:                            #(n,because of WHILE loop)
        if n[leng-1] == 0:                    #(n, because it is inside of WHILE loop)
            count+=1                          #(n, because it is inside of WHILE loop)
        leng-=1                               #(n, because it is inside of WHILE loop)
    return (count)                            (1)
    
'''Big 0 = 6n+5 = O(n)'''
 

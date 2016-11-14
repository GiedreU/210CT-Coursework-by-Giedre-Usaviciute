def factorial(num):

    if num > 1:
        return(num * factorial(num-1))
    elif num == 1:
        return(num)
    
def countZero(n):

    n = [int (i) for i in str(factorial(n))]
    count = 0
    leng = len(n)
    while leng!=0:
        if n[leng-1] == 0:
            count+=1
        leng-=1
    return (count)
    

zero = countZero(7)
print(zero)
 

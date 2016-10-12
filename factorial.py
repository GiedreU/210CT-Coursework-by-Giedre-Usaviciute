def factorial(num):

    if num > 1:
        return(num * factorial(num-1))
    else:
        return(num)
    
def countZero(n):

    n = [int (i) for i in str(factorial(n))]
    count = 0
    lenght = len(n)
    while n[lenght-1] == 0:
        count+=1
        lenght-=1
    return (count)
    

zero = countZero(10)
print(zero)
 

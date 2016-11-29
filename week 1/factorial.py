def factorial(num):
    '''recursive function that takes a number and returns a factorial of it by recursevely multiplying given number and number-1'''
    if num > 1:
        return(num * factorial(num-1))
    elif num == 1:
        return(num)
    
def countZero(n):
    '''counts number of trailing '0' og viven number factorial'''
    n = [int (i) for i in str(factorial(n))] #list containing fatorial number converted into a str
    count = 0
    leng = len(n)
    while leng!=0:#takes number and increases count if it is '0', loops until the end of list or number is not a zero
        if n[leng-1] == 0:
            count+=1
        leng-=1
    return (count)
    

zero = countZero(7)
print(zero)
 

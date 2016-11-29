def prime(n,k):
    '''returns True if given number n is prime and false if it is not'''
    if n < 2: #no prime numbers less than 2
        return False
    elif n == 2 or (k ==2 and n%k != 0):#when k=2, it means number is devidable only by itself and one and there is need to devide by 1
        return True
    elif n%k != 0:
        return prime(n, k-1)
    else:
        return False
n=16
number = prime(n, n-1)
print(number)

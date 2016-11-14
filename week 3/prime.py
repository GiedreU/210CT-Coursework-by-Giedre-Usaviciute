def prime(n,k):
    if n < 2:
        return False
    elif n == 2 or (k ==2 and n%k != 0):
        return True
    elif n%k != 0:
        return prime(n, k-1)
    else:
        return False
n=16
number = prime(n, n-1)
print(number)

def binary_search(aList, low, high):
    '''returns true if value within given interval is found, else returns false'''
    if len(aList)==0:
        return False
    mid = len(aList)//2
    if aList[mid]>= low and aList[mid]<=high:
        return True
    elif aList[mid] < low:
        return binary_search(aList[(mid+1):], low, high)
    elif aList[mid] > high:
        return binary_search(aList[:(mid-1)], low, high)

aList = [2,3,5,7,9,9,9,11,13]
low = 13
high = 14
answer = binary_search(aList, low, high)
print(answer)

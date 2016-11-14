def binary_search(aList, low, high):
    if len(aList)==0:
        return False
    mid = len(aList)//2
    if aList[mid]>= low and aList[mid]<=high:
        return True
    elif aList[mid] < low and len(aList) != 0:
        return binary_search(aList[(mid+1):], low, high)
    elif aList[mid] > high and len(aList) != 0:
        return binary_search(aList[:(mid-1)], low, high)

aList = [2,3,5,7,9,9,9,11,13]
low = 13
high = 14
answer = binary_search(aList, low, high)
print(answer)

def maxSequence (alist):
    count = 0
    new = []
    if len(alist) != 0:
        for item in range(0,len(alist)-1):
            if alist[item] < alist[item+1]:
                count+=1
                if alist[item+1] == alist[-1]:
                    new.append(count+1)
            elif alist[item] >= alist[item+1]:  
                new.append(count+1)
                count = 0
            
    maxSet = max(new)
    maxInd = new.index(maxSet)
    start = 0
    i=0
    while i != maxInd:
        start+=new[i]
        i+=1
    end = start+maxSet
    return(alist[start:end])
             
myList = [1,2,3,4,5,6,7,8,9,2,3,4,5,6,1,2,3,1,7,10,15,1]
subList = []
subList = maxSequence(myList)
print(subList)

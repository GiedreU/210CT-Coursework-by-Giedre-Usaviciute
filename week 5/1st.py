def maxSequence (alist):
    count = 0
    i=1
    item = 0
    new = []
    if len(alist) != 0:
        while item in range(len(alist)-1)#:
            if alist[item] <= alist[item+1]:
                count+=1
            elif alist[item] > alist[item+1]:
                alist[item] = count+1
                new.append(count+1)
                
                count = 0
            item +=1
    print(new)          
myList = [1,2,3,1,2,3,4,5,1,2,1]
wow = []
wow = maxSequence(myList)
print(wow)

from random import randint

def shuffleList(alist):

    shuffledList = [0]*len(alist)
    usedList=[]
    for i in alist:
        place = getRandomNumber(0,len(alist),alist.index(i),usedList)
        shuffledList[place]=i
    return shuffledList

def getRandomNumber(n,m,i,usedList):
    '''returns unused random number which will be used as place
    number to store variable from one list to another'''
    num = randint(n,m-1)
    if i == 0:
        usedList.append(num)
        return num
    else:
        if num in usedList:
            return getRandomNumber(n,m,i,usedList)
        else:
            usedList.append(num)
            return num

wow = [5,3,8,6,1,2,7]
a = shuffleList(wow)
print(a)


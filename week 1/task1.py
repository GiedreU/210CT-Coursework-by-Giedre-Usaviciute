from random import randint

def shuffleList(alist):
    '''for each item in given list randomly generates new index to which it will be stored in a new list. usedList is a list which is
    used to store already used index, to prevent repetition and overwriting '''
    shuffledList = [0]*len(alist)#new empty list to which all items are trasfered from the given list
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


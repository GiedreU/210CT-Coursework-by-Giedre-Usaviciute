def alienPrediction(x,y):
    
    dayList = [1]+[0]*29
    for day in range(len(dayList)-1):
        dayList[day+1] += dayList[day]
        if day < (30-y): dayList[day+y] += dayList[day]*x
    return dayList

         
print(alienPrediction(3,5))

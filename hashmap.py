tempList=[]
with open ('Sorting Algorithms/nyc_weather.csv','r') as f:
    for line in f:
        tokens=line.strip().split(',')
        tempList.append(tokens)

#print(tempList)
intList=[]
for i in range(len(tempList)):
    try:
        intList.append(int(tempList[i][1]))
    except:
        print('The value is not an integer')
print(intList)
#Finding average of the first week
sumFirstWeek=sum(intList[:7])
average=sumFirstWeek/7
maxTemp=max(intList)
print(maxTemp)
print('The average temp of first week is: {}'.format(average.__round__(2)))




class HashTable:  
    def __init__(self,arr):
        self.arr = arr
        self.MAX = len(arr)
        
    def __getitem__(self, item):
        for array in self.arr:
            if array[0]==item:
                return array[1]
 
tempList=[]
with open ('Sorting Algorithms/nyc_weather.csv','r') as f:
    for line in f:
        tokens=line.strip().split(',')
        tempList.append(tokens)
#print(tempList)
t=HashTable(tempList)
Jan1Value= t['Jan 1']
Jan4Value=t['Jan 4']
print('Our January First Value is {}'.format(Jan1Value))
print('Our January Fourth Value is {}'.format(Jan4Value))

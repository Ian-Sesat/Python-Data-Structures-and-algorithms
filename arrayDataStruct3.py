oddNum=[]
maxNo=input('Please enter your max number ')
maxNo=int(maxNo)
for i in range(1,maxNo+1):
    if i%2==1:
        oddNum.append(i)
print('Odd Numbers: {}'.format(oddNum))
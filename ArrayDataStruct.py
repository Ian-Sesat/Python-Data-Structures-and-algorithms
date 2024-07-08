#Exercise 1:
monthlyExpenses=[2200,2350,2600,2130,2190]
extra=monthlyExpenses[1]-monthlyExpenses[0]
print('The difference between February and January spend is ${}'.format(extra))
totalFirstQuarter=monthlyExpenses[0]+monthlyExpenses[1]+monthlyExpenses[2]
print('The total sum of the first quarter is ${}'.format(totalFirstQuarter))
for expense in monthlyExpenses:
    if expense==2000:
        text='You spent $2000 at a certain month'
        break
    else:
        text='You did not spend $2000 any single month'
print(text)
JuneSpend=1980
monthlyExpenses.append(JuneSpend)
print(monthlyExpenses)
monthlyExpenses[3]=monthlyExpenses[3]-200
print(monthlyExpenses)
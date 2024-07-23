#Recursion test case 1
def sum_of_list(arr):
    if len(arr)==0 :
        return None
    elif len(arr)==1 :
        return arr[0]
    else:
        return arr[0]+sum_of_list(arr[1:])
print(sum_of_list([1,2,3]))
#Case 2:
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
numberPower=power(3,4)
print(numberPower)
#Case 3:Python program to get the sum of a non-negative integer using recursion.
def get_digits(number):
    if number == 0:
        return
    else:
        digits.append(number % 10)  # Get the last digit
        number = number // 10       # Remove the last digit
        get_digits(number)
    digits.reverse()  # The digits are collected in reverse order
        
    return digits  
digits=[]
ourDigits=get_digits(545)
print(ourDigits)
print(sum_of_list(ourDigits))

def bubble_sort(elements,key):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a=elements[j][key]
            b=elements[j+1][key]
            if  a>b :
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

def main():
    elements = [
        { 'name': 'miley',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dan', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kristine',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'amerix',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
	#Sorting based on transaction_amount:
    bubble_sort(elements, key='transaction_amount')
    print('Sorting based on transaction amount returns: {}'.format(elements))
    #Sorting based on name:
    bubble_sort(elements, key='name')
    print('Sorting based on name returns: {}'.format(elements))
if __name__ == '__main__':
    main()
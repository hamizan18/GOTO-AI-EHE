array_bubble = [8, 3, 1, 6, 2, 9, 7, 4, 5]
array_selection = [2, 5, 4, 7, 8, 9, 1, 4, 3]

def bubbelSort():
    print('Array bubble sebelum bubble sort: ')
    for number in array_bubble:  
        print(number, end=" ")
    
    n = len(array_bubble)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array_bubble[j] > array_bubble[j+1]:
                array_bubble[j], array_bubble[j+1] = array_bubble[j+1], array_bubble[j]
                
    print('\nArray after bubble sort: ')
    for number in array_bubble:  
        print(number, end=" ")
    
def selectionSort():
    print('Array bubble sebelum selection sort: ')
    for number in array_selection:
        print(number, end=" ")
        
    n = len(array_selection)

    for i in range(n):
        for j in range(i, n - 1):
            if array_selection[j] > array_selection[j+1]:
                minNum = array_selection[j+1]
            else:
                minNum = array_selection[j]
            array_selection[j] = minNum
        
    print('\nArray after selection sort: ')
    for number in array_selection:  
        print(number, end=" ")
    
bubbelSort()
print('\n')
selectionSort()
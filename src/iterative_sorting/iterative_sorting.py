# TO-DO: Complete the selection_sort() function below 
testArray = [64, 25, 12, 22, 11]

def selection_sort( array ):
    # loop through n-1 elements
    
    for i in range(len(array)):
        # Create a variable to be used later, set it equal to whatever value I'm currently
        min_index = i
        print("min index inside first loop: ", min_index)
        for j in range (i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
                print("min index inside second loop: ", min_index)
        array[i], array[min_index] = array[min_index], array[i]         
    return array

print("selection sort: ", selection_sort(testArray))
        
# for i in range(len(mylist)):
#     for j in range(i + 1, len(mylist)):
#         compare(mylist[i], mylist[j])
  
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( array ):
    for i in range(len(array)):
        for j in range (i+1, len(array)):
            if array[j-1] > array[j] : 
                array[j-1], array[j] = array[j], array[j-1]
    return array

print("Bubble Sort: ", bubble_sort(testArray))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
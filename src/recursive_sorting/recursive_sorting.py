# TO-DO: complete the helper function below to merge 2 sorted arrays

# arr1 = [1,3,5,7]
# arr2 = [2,4,6,8]
# def merge( arrA, arrB, merged_arr = [] ):
#     #elements = len( arrA ) + len( arrB )
#     #merged_arr = [0] * elements
#     # TO-DO
    
#     if len(arrA) == 0 or len(arrB) == 0:
#         return merged_arr
#     elif arrA[0] < arrB[0]:
#         print("arrA", arrA[0])
#         merged_arr.append(arrA[0])
#         arrA.pop(0)
#         merge(arrA, arrB)
#     elif arrB[0] < arrA[0]:
#         print("arrB", arrB[0])
#         merged_arr.append(arrB[0])
#         arrB.pop(0)
#         merge(arrA, arrB)

# print("merge solution", merge(arr1, arr2))


# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
#     # TO-DO

#     return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)
print("fin", merge_sort(arr1))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

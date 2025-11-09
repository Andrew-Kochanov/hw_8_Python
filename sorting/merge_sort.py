from random import randint
import sys
sys.setrecursionlimit(100000)

def merge(left_array, right_array):
    index_left = 0
    index_right = 0
    lenght_left = len(left_array)
    lenght_right = len(right_array)
    sorted_array = []

    for i in range(lenght_left + lenght_right):
        if index_left < lenght_left and index_right < lenght_right:
            if left_array[index_left] <= right_array[index_right]:
                sorted_array.append(left_array[index_left])
                index_left += 1
            else:
                sorted_array.append(right_array[index_right])
                index_right += 1
        elif index_right == lenght_right:
            sorted_array.append(left_array[index_left])
            index_left += 1
        elif index_left == lenght_left:
            sorted_array.append(right_array[index_right])
            index_right += 1
    return sorted_array

def merge_sort(array):
    if len(array) < 2:
        return array
    pivot = len(array) // 2
    left_array = merge_sort(array[:pivot])
    right_array = merge_sort(array[pivot:])
    return merge(left_array, right_array)
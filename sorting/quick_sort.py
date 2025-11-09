from random import randint

def partition(array, low, high):
    pivot_value = array[randint(low, high)]
    l = low - 1
    h = high + 1
    while l < h:
        l += 1
        while array[l] < pivot_value:
            l += 1
        h -= 1
        while array[h] > pivot_value:
            h -= 1
        if l >= h:
            return h
        array[l], array[h] = array[h], array[l]

def quick_sorting(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sorting(array, low, pivot)
        quick_sorting(array, pivot + 1, high)

def quick_sort(array):
    quick_sorting(array, 0, len(array) - 1)
    return array
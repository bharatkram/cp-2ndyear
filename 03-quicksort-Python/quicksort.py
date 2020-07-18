"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i+1


def qsort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        qsort(array, low, pi - 1)
        qsort(array, pi + 1, high)


def quicksort(array):
    # Your code goes here
    qsort(array, 0, len(array) - 1)
    return array

#!/usr/bin python3
from is_sorted import is_sorted # Don't import this if you don't have the file

def bubble_sort(arr):
    length = range(len(arr) - 1)
    while is_sorted(arr) == False:
        for i in length:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                #Swap pseudo version
                #temp = arr[i]
                #arr[i] = arr[i+1]
                #arr[i+1] = temp
    else:
        return arr

def selection_sort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i] ,arr[minIdx] = arr[minIdx], arr[i]
    return arr

#!/usr/bin python3

def binary_search(arr,target):
    low = 0 # lower limit
    high = len(arr) - 1 # upper limit
    while low <= high:
        mid = (low + high) // 2 # mid-point
        if arr[mid] == target: # Check if I find the target
            return mid
        # Code below only exec if target is not found
        elif arr[mid] < target: #Cut off 1/2 of the array
            low = mid + 1
        elif arr[mid] > target: # Same as above
            high = mid - 1
    else:
        return False

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return False

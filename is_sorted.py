#!/usr/bin python3
# This function can check if an array is sorted in ascending order
# Credit: Him/SLBG128

def is_sorted(arr):
    length = range(len(arr) - 1)     # get the length/size of array
    for i in length:
        if arr[i] > arr[i+1]:        # To check in descending order, change the '>' to '<'
            return False
    else:
        return True

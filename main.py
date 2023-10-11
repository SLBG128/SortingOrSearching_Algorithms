#!/usr/bin python3
# This is a tesing file that test the algorithms ~Him/SLBG128
#from is_sorted import is_sorted
from search_algorithms import *
from sorting_algorithms import *

def main():
    arr = [5,8,2,5,9,10,4,27,15,19,1,5,20,30,24,10,37,18,10,50]
    b_sorted = bubble_sort(arr)
    s_sorted = selection_sort(arr)
    print("Bubble Sort:   ", b_sorted)
    print("Selection Sort:", s_sorted)
    if b_sorted != s_sorted:
        print("Something went wrong......") # If this occur, please contact SLBG128/Him
        return 
    new_arr = b_sorted
    target = 18
    idx_b = binary_search(new_arr,target)
    idx_l = linear_search(new_arr,target)
    if idx_b != False:
        print(f"Binary Search: Target found on index {idx_b}")
    else:
        print(f"Binary Search: {idx_b} does not exist on the array")
    if idx_l != False:
        print(f"Linear search: Target found on index {idx_l}")
    else:
        print(f"Linear Search: {idx_l} does not exist in the array")

if __name__ == "__main__":
    main()

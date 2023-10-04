#!/usr/bin python3

def binary_search(arr,target):
    low = 0 # lower limit
    high = len(arr) - 1 # upper limit
    found = False # Is the target found?
    
    while found == False:
        mid = (low + high) // 2 # mid-point
        if arr[mid] == target: # Check if I find the target
            print(f"Target exist at index {mid}")
            found = True
        # Code below only execute if the target is not find
        elif low >= high: # Check existance by comparing limits
            print(f"{target} does not exist in the list")
            break
        elif arr[mid] < target: #Cut off 1/2 of the array
            low = mid + 1
        elif arr[mid] > target: # Same as above
            high = mid - 1

def main():
    arr = [2,6,10,13,16,18,19,22,25,26,29,30] # Test data
    target = int(input("What is the number you want to find in the list?"))
    binary_search(arr,target)

if __name__ == "__main__":
    main()

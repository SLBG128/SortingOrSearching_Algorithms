def binarySearch(arr,target):
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
    return False

# Testing data
arr = [2,6,7,9,10,14,17,22,25,28,30,36,49]
existTarget = 14
nonExistTarget = 15
# Test if it can find existing target
x = binarySearch(arr,existTarget)
if x is not False:
    print(f"Target found on index {x}")
else:
    print(f"{existTarget} does not exist on the array")
# Test if it can return target that is not existing
y = binarySearch(arr,nonExistTarget)
if y is not False:
    print(f"Target found on index {y}")
else:
    print(f"{nonExistTarget} does not exist on the array")

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return False

# Testing data
arr = [2,6,7,9,10,14,17,22,25,28,30,36,49]
existTarget = 14
nonExistTarget = 15
# Test if it can find existing target
x = linearSearch(arr,existTarget)
if x is not False:
    print(f"Target found on index {x}")
else:
    print(f"{existTarget} does not exist on the array")
# Test if it can return target that is not existing
y = linearSearch(arr,nonExistTarget)
if y is not False:
    print(f"Target found on index {y}")
else:
    print(f"{nonExistTarget} does not exist on the array")

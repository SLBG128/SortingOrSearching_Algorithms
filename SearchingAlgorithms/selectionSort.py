def is_sorted(arr):
    length = range(len(arr) - 1)     # get the length/size of array
    for i in length:
        if arr[i] > arr[i+1]:        # To check in descending order, change the '>' to '<'
            return False
    else:
        return True

def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i] ,arr[minIdx] = arr[minIdx], arr[i]
    return arr

# Test data
arr = [5,8,2,7,9,10,4,27,15,19,1,5,20,30,24,3,37,18,10,50]
sortedArray = selectionSort(arr)
print(sortedArray)

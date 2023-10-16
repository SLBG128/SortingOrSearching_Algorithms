def is_sorted(arr):
    length = range(len(arr) - 1)     # get the length/size of array
    for i in length:
        if arr[i] > arr[i+1]:        # To check in descending order, change the '>' to '<'
            return False
    else:
        return True


def bubbleSort(arr):
    length = range(len(arr) - 1)
    while is_sorted(arr) is False:
        for i in length:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                #Swap pseudo version
                #temp = arr[i]
                #arr[i] = arr[i+1]
                #arr[i+1] = temp
    else:
        return arr

# Test data
arr = [5,8,2,7,9,10,4,27,15,19,1,5,20,30,24,3,37,18,10,50]
sortedArray = bubbleSort(arr)
print(sortedArray)

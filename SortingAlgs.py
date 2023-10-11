#!/usr/bin python3

def is_sorted(arr):            #Check if the array/list is sorted
    length = range(len(arr) - 1) # get the length of array
    for i in length:
        if arr[i] > arr[i+1]:
            return False
    else:
        return True

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


def main():
    arr = [2,5,8,2,6,6,12,22,17,19] #test data
    bsort = bubble_sort(arr)
    print(bsort)
    ssort = selection_sort(arr)
    print(ssort)

if __name__ == "__main__":
    main()

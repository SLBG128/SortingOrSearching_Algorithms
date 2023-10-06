#!/usr/bin python3

def is_sorted(arr):
    length = range(len(arr) - 1)
    for i in length:
        if arr[i] > arr[i+1]:
            return False
    else:
        return True

def bubble_sort(arr):
    length = range(len(arr) - 1)
    sorted = False
    while sorted == False:
        for i in length:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                # Swap pseudo version
                #temp = arr[i]
                #arr[i] = arr[i+1]
                #arr[i+1] = temp
        if is_sorted(arr) == True:
            sorted == True
            print(arr)
            break

def main():
    arr = [2,5,8,2,6,6,12,22,17,19] #test data
    bubble_sort(arr)

if __name__ == "__main__":
    main()

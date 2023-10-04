#!/usr/bin python3

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Target found at index {i}")
            break
    else:
        print(f"{target} does not exist in the array")

def main():
    arr = [2,4,7,8,10,13,17,20] # Test data
    target = int(input("What is the number you want to find in the list?"))

    linear_search(arr,target)

if __name__ == "__main__":
    main()

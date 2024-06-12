def BS_iterative(arr, target):
    low = 0
    high = len(arr) - 1 
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid -1
    return -1


if __name__ == "__main__":

    array = [1,2,3,4,5,6,7,8,9]
    target = 5

    result = BS_iterative(array, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
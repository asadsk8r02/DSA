# Iterative approach

def First_Occurance(arr, target):
    low = 0
    high = len(arr) - 1
    while (low<=high):
        mid = (low+high)//2
        if target > arr[mid]:
            low = mid+1
        elif target < arr[mid]:
            high = mid-1
        else:
            if (mid == 0) or (arr[mid-1] != arr[mid]):
                return mid
            else:
                high = mid-1

    return -1

# Driver code
if __name__ == "__main__":
    
    arr = [5,10,10,10,20,20,20,20,20,30,30,30,30,30,40,40,40]
    target = 20

    result = First_Occurance(arr, target)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not in the list")
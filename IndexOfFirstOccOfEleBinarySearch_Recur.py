# Recursive approach

def First_Occurance(arr, target, low, high):
    if low > high:
        return -1
    mid  = (low + high)//2
    if target > arr[mid]:
        return First_Occurance(arr, target, mid+1, high)
    elif target < arr[mid]:
        return First_Occurance(arr, target, low, mid-1)
    else:
        if (mid == 0) or (arr[mid -1] != arr[mid]):
            return mid
        else:
            return First_Occurance(arr, target, low, mid-1)

# Driver code
if __name__ == "__main__":
    
    arr = [5,10,10,10,20,20,20,20,20,30,30,30,30,30,40,40,40]
    target = 20

    result = First_Occurance(arr, target, 0, len(arr)-1)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not in the list")
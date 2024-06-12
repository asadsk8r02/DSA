# Recursive approach

def Last_Occurance(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if target > arr[mid]:
        return Last_Occurance(arr, target, mid+1, high)
    elif target < arr[mid]:
        return Last_Occurance(arr, target, low, mid-1)
    else:
        if (mid==len(arr)-1) or (arr[mid+1]!=arr[mid]):
            return mid
        else:
            return Last_Occurance(arr, target, mid+1, high) 

# Driver code
if __name__ == "__main__":
    
    arr = [5,10,10,10,20,20,20,20,20,30,30,30,30,30,40,40,40]
    target = 10

    result = Last_Occurance(arr, target, 0, len(arr)-1)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not in the list")
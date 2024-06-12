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

def CountOccurance(arr, target):
    first = First_Occurance(arr, target, 0, len(arr)-1)
    if first == -1:
        return 0
    last = Last_Occurance(arr, target, 0, len(arr)-1)
    return last - first + 1
    
    
# Driver code

if __name__ == "__main__": 
    
    arr = [5,10,10,10,10,10,10,10,20,20,20,30,40]
    target = 10

    result = CountOccurance(arr, target)

    if result != -1:
        print(f"{target} count is {result}")
    else:
        print(f"{target} not found")

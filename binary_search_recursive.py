def BS_recursive(arr, target, low , high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif target>arr[mid]:
        return BS_recursive(arr, target, mid+1, high)
    else:
        return BS_recursive(arr, target, low, mid-1)
    

if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7,8,9]
    target = 1

    result = BS_recursive(arr, target, 0 , len(arr)-1)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")

    
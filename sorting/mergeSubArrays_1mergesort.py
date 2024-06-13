# Sorted, Unsorted in single array/list
# Low, Mid, High ---> low <= mid < high
# low is movable and can be anywhere in the list/array

def mergesubarrays(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while i<len(left) and j < len(right):
        if left[i] <= right[j]: # <= for stable mergesort algo
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i<len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j<len(right):
        arr[k] = right[j]
        k += 1
        j += 1

    return arr

# Driver code 
if __name__ == "__main__":
    arr = [10,15,20,40,8,11,13,55]
    result = mergesubarrays(arr,0,3,7) #We cannot determine low in this code so we gave mid by visual look as 3rd Index, since we need both sorted subarrays whcih are [10,15,20,40] and [8,11,13,55]
    print(f"Sorted subarrays is {result}")





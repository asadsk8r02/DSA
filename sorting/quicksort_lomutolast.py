#  Quick sort with Lomuto Partition

# L --- < pivot ---- i ----- >= pivot ----- j ---Yet to be determined---- H

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j]<=pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n - 1)
    print("Sorted array is:", arr)  

    

# Pivot element is the first element

# L --- <= Pivot ---- i ----- Yet to be determined ----- j ---- >= pivot ---- H

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)
        quicksort(arr, low, p)
        quicksort(arr, p + 1, high)

# Driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n - 1)
    print("Sorted array is:", arr)

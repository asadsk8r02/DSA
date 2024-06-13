# List.sort() and sorted(List) uses "TIMSORT" Alogirthm which is a hybrid algo derived from merge sort and insertion sort.

# L.sort(key = Any function, reverse = True/False) is applied on List only and does inplace sorting.

# sorted(L, key = Any function, reverse = True/False) always return a NEW LIST and can be applied on any iterable(list, string, tuple) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.

# .sort()
unsorted_list = [2,4,5,32,6,255,5,42]
unsorted_list.sort()

# Sorted()
x = ['q', 'w', 'r', 'e', 't', 'y'] 
print(sorted(x))

# A stable sorting algorithm maintains the relative order of records with equal keys (or values). This means that if two elements are equal in value, their original order in the input list will be preserved in the sorted list.

# Stable Algorithms - Merge sort, Bubble sort, Insertion sort. --> BIM
# Unstable Algorithm - Selection Sort, Quick sort, Heap Sort. --> HSQ


# TIMSORT Algorithm - Stable Algo 

MIN_MERGE = 32

def calc_min_run(n):
    """Returns the minimum length of a run from 23 - 64 so that
    the array of n elements can be divided into an array of runs
    of length MIN_MERGE or less, such that the number of runs
    is minimal"""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    """Sorts array from the left index to the right index which is of size at most MIN_MERGE"""
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    """Merges the sorted runs"""
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    
    i, j, k = 0, 0, l

    # After comparing, we merge those two sorted sub-arrays
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left[], if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right[], if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)

    # Sort individual sub-arrays of size RUN
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = min_run
    while size < n:
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] & arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

# Example usage
arr = [5891, 462, 1012, 288, 2897, 4607, 3883, 2095, 7746, 3155, 4495, 6157, 1267, 3484, 5676, 5714, 2827, 5702, 4631, 4010, 8120, 778, 8186, 503, 3833, 3500, 8287, 6136, 547, 121, 6031, 5545, 5661, 6773, 4663, 5283, 4600, 964, 7615, 1885]

tim_sort(arr)
print(arr)





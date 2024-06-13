# Divide, Conquer, and merge
# Stable algo
# O(NlogN)time and O(N) space.
# Well suited for linked list and works well in O(1) time.
# Used in external sorting
# In general for arrays, Quicksort outperforms
#  Not an inplace algo but there are variants of merge sort like BLOCKMERGE SORT wichi are inplace.

# left <= mid < right

# Pseudo code according to GFG part 1 and part2
# def mergesort(arr,left,right):
#     if right > left:
#         mid = (left+right)//2
#         mergesort(arr,left, mid)
#         mergesort(arr,mid+1,right)
#         merge(arr,left, mid, right)

def merge(left, right):
    merged = []
    m = len(left)
    n = len(right)
    i = 0
    j = 0
    while i<m and j<n:
        if left[i]<=right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i<m:
        merged.append(left[i])
        i += 1
    while j<n:
        merged.append(right[j])
        j += 1

    return merged

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

    
# Driver code 
if __name__ == "__main__":
    arr = [10,30,5,15,7]
    result = mergesort(arr)
    print(f"Sorted list is {result}")
    

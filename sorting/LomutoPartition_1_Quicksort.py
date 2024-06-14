# Pivot element is the last element

# L --- < pivot ---- i ----- >= pivot ----- j ---Yet to be determined---- H

def LomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1, arr

# Driver code
if __name__ == "__main__":
    arr = [10,80,30,90,50,70]
    idx, result = LomutoPartition(arr,0,len(arr)-1)
    print(f"The pivot index is {idx} and the arr is {result}")

# Pivot element is the first element 
# It is not gaurenteed that pivot element 

# L --- <= Pivot ---- i ----- Yet to be determined ----- j ---- >= pivot ---- H

def HoarePartition(arr, l, h):
    pivot = arr[l]
    i = l-1
    j = h+1
    while True:
        i += 1
        while arr[i]<pivot:
            i += 1
        j -= 1
        while arr[j]>pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


# Driver code
if __name__ == "__main__":
    arr = [5,3,8,4,2,7,1,10]
    result = HoarePartition(arr, 0, len(arr)-1)
    print(f"The resulting arr is {result}")



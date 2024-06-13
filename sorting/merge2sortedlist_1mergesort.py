# O(m + n)

def mergesortedlists(a,b):
    result = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i<m and j<n:
        if a[i]>b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i]) 
            i += 1
    while i<m:
        result.append(a[i])
        i += 1
    while j<n:
        result.append(b[j])
        j += 1
    return result

# Driver code
if __name__ == "__main__":
    arr1 = [1,5,7,8]
    arr2 = [1,2,4,4,7]
    result = mergesortedlists(arr1,arr2)
    print(f"Merged list is: {result} ")
    

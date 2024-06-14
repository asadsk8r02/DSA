# Optimization of Selection osrt algo
# Build a heap map
# Repeated swap root with last node, reduce heap size by 1 and heapify --> O(logN).
# O(NlogN)
# Not stable
# Used in hybrid sorting algorithm e Intrasort 
# Increasing (Max heap) and Decreasing (Min Heap)

# ================================================================================================================
### Heapify 
# ================================================================================================================
## In a binary heap:
    # The elements are stored in an array in a level-order (breadth-first) manner. (left to right)
    # The root of the heap is at index 0.

# For any node at index i:
    # The left child is at index 2 * i + 1.
    # The right child is at index 2 * i + 2.

# All leaf nodes are in the second half of the array.
# All non-leaf nodes are in the first half of the array.
# ================================================================================================================

## Calculating the Last Non-Leaf Node
    # The total number of elements in the array is n.
    # The last non-leaf node is the parent of the last element in the array.

# Determining the Parent of the Last Element
    # Index of the Last Element: The last element in an array of size n is at index n - 1.

# Parent of the Last Element:
    # For an element at index i, its parent is at index (i - 1) // 2.
    # Thus, the parent of the last element (which is at index n - 1) is at index (n - 1) // 2.

# Adjusting for the Last Non-Leaf Node
    # Since the array is 0-indexed:
    # The formula to find the last non-leaf node becomes: n // 2 - 1.

# ================================================================================================================

# Max or Min heap
# Step 1: Identify the Last Non-Leaf Node
# Step 2: Heapify from the Last Non-Leaf Node Upwards

# ================================================================================================================

# Increasing (Max heap)
# Heapsort for increasing sort

def maxheapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right <n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxheapify(arr, n, largest)

def buildmaxheap(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        maxheapify(arr,n,i)

# Build a Max-Heap: Convert the array into a max-heap.
# Extract Elements: Extract the largest element from the heap, place it at the end of the array, and reduce the size of the heap. Repeat this process until all elements are extracted.

def heapsortinc(arr):
    n = len(arr)
    buildmaxheap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxheapify(arr,i,0)

# Driver code
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1, 2, 7, 6]
    heapsortinc(arr)
    print(f"The increasing sorted array is {arr}")

# ================================================================================================================

# Decreasing (Max heap)
# Heapsort for Decreasing sort

def minheapify(arr, n, i):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minheapify(arr, n, smallest)

def buildminheap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        minheapify(arr,n,i)

def heapsortdec(arr):
    n = len(arr)
    buildminheap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        minheapify(arr,i,0)

# Driver code
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1, 2, 7, 6]
    heapsortdec(arr)
    print(f"The decreasing sorted array is {arr}")
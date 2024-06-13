# O(N^2) - Worst case - reverse sorted
# O(N) - Best Case - sorted
# Inplace algo
# Used in practice for small arrays (Timsort and Intrasort)

#  Sorted and Unsorted array concept

class Insertionsort:
    def insertion(self, arr):
        N = len(arr)
        for i in range(1,N):
            insertion_ele = arr[i]
            j = i - 1
            while j>=0 and insertion_ele < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = insertion_ele

        return arr
    
# Driver code
if __name__ == "__main__":
    arr = [10,5,3,5,7,25,6,40,1]
    sorter = Insertionsort()
    result = sorter.insertion(arr)
    print(f"Sorted list is {result}")

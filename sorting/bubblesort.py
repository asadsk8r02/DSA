# O(N^2) - Worst case reverse sorted
# O(N) - Best case sorted
# Multiple Passes
# Not very practical application
# Stabel and swaps adjacent data

class Bubblesort:
    def __init__(self) -> None:
        pass

    def bubble(self, arr):
        N = len(arr)
        for i in range(0,N-1):
            swapped = False
            for j in range(0, N-i-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break

        return arr
        
# Driver code
if __name__ == "__main__":
    arr = [2,10,8,7,15,2,4,5]
    sorter = Bubblesort()
    result = sorter.bubble(arr)
    print(f"Sorted arry is {result}")
            
        
    
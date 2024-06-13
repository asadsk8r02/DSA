# Theta(N^2) time in all cases
# Unsatable algo
# Inplace algo

class Selectionsort:
    def selection(self, arr):
        N = len(arr)
        for i in range(N-1):
            min_idx = i
            for j in range(i+1,N):
                if arr[j]<arr[min_idx]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        return arr
    
# Driver code
if __name__ == "__main__":
    arr = [10,5,8,20,2,8,3,1]
    sorter = Selectionsort()
    result = sorter.selection(arr)
    print(f"Sorted list is {result}")

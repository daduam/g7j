class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            jmin = i
            for j in range(i+1, n):
                if arr[j] < arr[jmin]:
                    jmin = j
            if jmin != i:
                arr[i], arr[jmin] = arr[jmin], arr[i]

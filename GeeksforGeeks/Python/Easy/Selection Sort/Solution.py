class Solution: 
    def selectionSort(self, arr):
        n=len(arr)
        for counter in range (1,n):
            is_sorted = False
            for j in range (1,n):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    is_sorted = True 
            if not is_sorted :
                break
        
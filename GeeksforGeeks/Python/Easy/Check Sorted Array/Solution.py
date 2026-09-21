class Solution:
    def isSorted(self, arr):
        is_sorted=True  
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                is_sorted = False 
                break
        return is_sorted
        
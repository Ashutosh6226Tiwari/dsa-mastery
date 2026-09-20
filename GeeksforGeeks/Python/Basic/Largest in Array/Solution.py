class Solution:
    def largest(self, arr):
        largest =-1
        for i in range(len(arr)):
            if arr[i] > largest :
                largest = arr[i] 
        return largest 
        

class Solution:
    def search(self, arr, x):
        for i in range (0,len(arr)):
            if arr[i]==x:
                index =i
                break
            else :
                index=-1
        return index
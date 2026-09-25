class Solution:
    def countFreq(self, arr, target):
        count =0
        for i in range (0,len(arr)):
            if arr[i]==target:
                count+=1
        return count
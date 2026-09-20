class Solution:
    def getSecondLargest(self, arr):
        largest = arr[0]
        second_largest=-1 
        for i in range(len(arr)):
            if arr[i]>largest:
                second_largest= largest
                largest= arr[i]
                
        for num in arr:
            if num != largest and num > second_largest:
                second_largest = num
                
        return second_largest
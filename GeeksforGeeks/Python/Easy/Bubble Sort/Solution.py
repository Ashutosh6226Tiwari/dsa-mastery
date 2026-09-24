class Solution:
    def bubbleSort(self,arr):
        # for i in range (0,len(arr)-1):
        #     if (arr[i]>arr[i+1]):
        #         arr[i],arr[i+1]=arr[i+1],arr[i]
    
        # return arr
        
        for i in range (1, len(arr)):
            if (arr[i]<arr[i-1]):
                arr[i],arr[i-1]=arr[i-1],arr[i]
        
            
class Solution:
    def bubbleSort(self,arr):
        # n=len(arr)
        # for counter in range (1,n):
        #     for i in range (0,n-1):
        #         if (arr[i]>arr[i+1]):
        #             arr[i],arr[i+1]=arr[i+1],arr[i]
        
        #     return arr
        
        n=len(arr)
        for i in range (1, n):
            is_swap=False
            for j in range (1,n):
                if (arr[j]<arr[j-1]):
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    is_swap=True
                    
            if not is_swap :
                break
            
          
    
            
    
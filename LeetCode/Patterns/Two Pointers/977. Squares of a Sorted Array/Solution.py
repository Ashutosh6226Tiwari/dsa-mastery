class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for num in nums :
            ans.append(num**2)
        ans.sort()
        return ans
        
# <--------------------------------------------------->


        # left, right = 0 , len(nums)-1
        # output=[0]*len(nums) 

        # while left <= right :
        #     left**=2
        #     right**=2
        #     if left<right:
        #         output.append[right]
        #         right-=1
            
        #     elif right < left :
        #         output.append(left)
        #         left+=1

        #     return output


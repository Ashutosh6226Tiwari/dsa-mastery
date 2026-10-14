class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # ans=[]
        # for num in nums :
        #     ans.append(num**2)
        # ans.sort()
        # return ans
        
# <--------------------------------------------------->


        n= len(nums)
        left, right = 0 , n-1
        output=[0]*n 
        k=n-1

        while left <= right :
            l_square=nums[left]*nums[left]
            r_square=nums[right]*nums[right]
            
            if l_square<r_square:
                output[k]=r_square
                right=right-1
            else:
                output[k]=l_square
                left=left+1
            k=k-1

        return output


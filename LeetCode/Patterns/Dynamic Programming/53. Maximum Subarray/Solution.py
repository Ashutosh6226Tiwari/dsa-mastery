class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest_sum=-1001  
        for i in range (0,len(nums)):
            curr_sum=0
            for j in range (i, len (nums)):
                curr_sum+=nums[j]
                
                if curr_sum >largest_sum:
                    largest_sum=curr_sum
        return largest_sum

        
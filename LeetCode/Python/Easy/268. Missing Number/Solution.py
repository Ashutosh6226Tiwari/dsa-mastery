class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        total= (n*(n+1))//2
        curr_sum=sum(nums)
        return total - curr_sum
        
        
        
        # n=len(nums)
        # nums.sort()
        # for i in range (n):
        #     if i !=nums[i]:
        #         return i
        # return n


        
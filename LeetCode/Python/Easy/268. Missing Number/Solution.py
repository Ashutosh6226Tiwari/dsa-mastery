class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # n=len(nums)
        # total= (n*(n+1))//2
        # curr_sum=sum(nums)
        # return total - curr_sum

        n=len(nums)
        total=0
        curr_sum=0
        for i in range (n+1):
            total+=i
        for i in range (n):
            curr_sum+=nums[i]
        return total - curr_sum
        
        # or
        # n=len(nums)
        # nums.sort()
        # for i in range (n):
        #     if i !=nums[i]:
        #         return i
        # return n


        
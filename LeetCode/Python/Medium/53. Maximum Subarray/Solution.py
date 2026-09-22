class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest_sum=curr_sum=nums[0]
        for i in range (1,len(nums)):
            if curr_sum+nums[i]>nums[i]:
                curr_sum+=nums[i]
            else:
                curr_sum=nums[i]
            largest_sum=max(curr_sum, largest_sum)
        return largest_sum

        


        # largest_sum=curr_sum =nums[0]   # start with first element
        #                                 # traverse from second element
        # for i in range (1,len(nums)):
        #     curr_sum=max(nums[i], nums[i]+curr_sum)
        #     largest_sum=max(curr_sum, largest_sum)
        # return largest_sum




        # largest_sum=-1001
        # for i in range (0,len(nums)):
        #     curr_sum=0
        #     for j in range (i , len(nums)):
        #         curr_sum+=nums[j]

        #         if curr_sum>largest_sum:
        #             largest_sum=curr_sum
        # return largest_sum






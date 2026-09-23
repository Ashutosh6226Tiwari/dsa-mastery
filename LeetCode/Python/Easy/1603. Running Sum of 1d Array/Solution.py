class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
        

        # ans = []
        # current = 0
        # for i in range(len(nums)):
        #     current += nums[i]   # keep adding to current
        #     ans.append(current)  # store the running sum
        # return ans

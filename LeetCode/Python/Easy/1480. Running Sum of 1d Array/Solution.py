class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans=[]
        current=0
        for i in range (0,len(nums)):
            current+=nums[i]
            ans.append(current)
        return ans 
        
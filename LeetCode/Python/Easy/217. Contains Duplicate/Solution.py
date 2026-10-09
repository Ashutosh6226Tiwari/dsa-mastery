class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        left=0
        right=n-1
        for i in range (n):
            if nums[left]==nums[right]:
                return True
            left+=1
            right-=1

        return False
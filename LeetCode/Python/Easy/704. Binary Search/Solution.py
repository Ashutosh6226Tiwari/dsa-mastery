class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for x, num in enumerate(nums):
            if num == target:
                return x
            
        return -1

        
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        return nums[n-k]

        
        # nums.sort(reverse=True)
        # return nums[k-1]
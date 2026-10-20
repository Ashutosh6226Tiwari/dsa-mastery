class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n=len(nums)
        l = curr = 0 

        while curr < n:
            if nums[curr]!=0:
                nums[curr],nums[l] = nums[l] ,nums[curr]        
                l+=1
            curr+=1

# time complexity = O(n)
# space complexity = O(1)













        
        
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        l=curr=1
        while curr<n:
            if nums[curr]!=nums[curr-1]:
                nums[l]=nums[curr]
                l+=1
            curr+=1
        return l


        # while curr<n:
        #     if nums[curr]==nums[curr-1]:
        #         curr+=1

        #     else:
        #         nums[l]=nums[curr]
        #         curr+=1
        #         l+=1













        
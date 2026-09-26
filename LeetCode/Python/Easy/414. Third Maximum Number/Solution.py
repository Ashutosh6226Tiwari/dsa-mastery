class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        temp=list(set(nums))
        temp.sort(reverse=True)
        n=len(temp)
        if n>=3 :
            return temp[2]
        return temp[0]
        


        # n=len(nums)
        # nums=set(nums)
        # if n>=3:
        #     return nums[3]
        
        
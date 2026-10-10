class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for num in nums :
            ans.append(num**2)
        ans.sort()
        return ans
        
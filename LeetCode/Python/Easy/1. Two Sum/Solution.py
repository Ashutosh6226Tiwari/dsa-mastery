class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i in range (0,len(nums)):
            data=target-nums[i]
            if data in hashmap:
                return [i,hashmap[data]]
            hashmap[nums[i]]=i

# brute force by hashmap 
#         hashmap={}
#         for i in range (0,len(nums)):
#             hashmap[nums[i]]=i
        
#         for i in range (0,len(nums)):
#             data = target-nums[i]
#             if data in hashmap and i!=hashmap[data]:
#                 return [i,hashmap[data]]

# brute force                    
#         n=len(nums)
#         for i in range (0,n-1):
#             for j in range (i+1,n):
#                 if nums[i]+nums[j]==target :
#                     return [i,j]
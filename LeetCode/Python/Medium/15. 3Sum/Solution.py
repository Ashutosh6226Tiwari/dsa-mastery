class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() 
        answer=[]
        for curr in range (0,len(nums)-2):
            if curr>0 and nums[curr]==nums[curr-1]:
                continue
            left , right  ,target = curr+1 , len(nums)-1 , -nums[curr]
            while left<right:
                curr_sum=nums[left]+nums[right]
                if target== curr_sum :
                    answer.append([nums[curr], nums[left] , nums[right]])

                    left+=1
                    while left<right and nums[left] == nums[right]:
                        left+=1

                    right-=1
                    while left<right and nums[left] == nums[right]:
                        right-=1

                elif  curr_sum < target:
                    left+=1

                else:
                    right-=1
            
        return answer 








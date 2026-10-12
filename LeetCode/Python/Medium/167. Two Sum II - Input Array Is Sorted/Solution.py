class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # hashmap={}
        # for i in range (0,len(numbers)):
        #     data= target -numbers[i]
        #     if data in hashmap:
        #         return [hashmap[data]+1,i+1]
            
        #     hashmap[numbers[i]]=i
                
        # hashmap={}
        # for i ,num in enumerate (numbers):
        #     data= target - num
        #     if data in hashmap :
        #         return [hashmap[data]+1, i+1]
        #     hashmap[num]=i

        left , right = 0 ,len(numbers)-1
        while left < right :
            s=numbers[left]+numbers[right]
            if target == s:
                return [left+1,right+1]

            elif s<target :
                left+=1

            else :
                right-=1   






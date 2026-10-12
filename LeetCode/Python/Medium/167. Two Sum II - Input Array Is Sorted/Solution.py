class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap={}
        for i in range (0,len(numbers)):
            data= target -numbers[i]
            if data in hashmap:
                return [hashmap[data]+1,i+1]
            
            hashmap[numbers[i]]=i
                
        
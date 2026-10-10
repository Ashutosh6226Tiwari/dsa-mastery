class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hashmap={}
        result=[]
        for num in nums :
            hashmap[num]=hashmap.get(num,0)+1
        for key,value in hashmap.items():
            if value > len(nums)//3: 
                result.append(key)
        return result        
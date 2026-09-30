class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashmap={}
        result=[]
        for num in nums2:
            hashmap[num]=hashmap.get(num,0)+1

        for num in nums1:
            if hashmap.get(num,0) >0:
                result.append(num)
                del hashmap[num]

        return result
        
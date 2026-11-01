class Solution:
    def singleNumber(self, nums: list[int]) -> int:

# by XOR                                     tc = O(n) , sc = O(1)

        # result =0
        # for num in nums :
        #     result = result ^ num
        # return result 

# by hashmap                                  tc = O(n)  , sc = O(n)
        hashmap={}
        for num in nums :
            hashmap[num]=hashmap.get(num , 0 )+1

        # for num in hashmap:
        #     if hashmap[num]==1:
        #         return num


        for num , count in hashmap.items():
            if count==1:
                return num

        
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count=0
        freq={}
        for num in nums :
            count+=freq.get(num-k,0)
            count+=freq.get(num+k,0)
            freq[num]=freq.get(num,0)+1
        return count

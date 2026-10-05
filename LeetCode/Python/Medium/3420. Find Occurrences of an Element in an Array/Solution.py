from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        # find all indices where x occurs
        indices = [i for i, val in enumerate(nums) if val == x]
        
        # for each query, return the index-th occurrence if it exists, else -1
        result = []
        for q in queries:
            if q <= len(indices):
                result.append(indices[q-1])  # queries are 1-based
            else:
                result.append(-1)
        return result

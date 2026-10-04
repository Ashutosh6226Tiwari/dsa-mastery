class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        hashmap={}
        counter=1
        for i in range (0, len(nums)):
            if nums [i]==x:
                hashmap[counter]=i
                counter+=1

        output=[-1]*len(queries)
        for i in range(0,len(queries)):
            if queries[i] in hashmap :
                output[i]=hashmap.get(queries[i])
        
        return output

        
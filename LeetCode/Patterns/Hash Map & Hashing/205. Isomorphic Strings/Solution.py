class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s ,map_t  = {} ,{}
        for i ,j in zip (s,t ):
            if i in map_s and map_s[i]!= j :
                return False 
            if j in map_t and map_t[j]!=i:
                return False
            map_s[i]=j
            map_t[j]=i
        return True 
            
            



            



        # hashmap={}
        # hashset=set()
        # for i in range (0, len (s)):
        #     if s[i] in hashmap :
        #         if t[i]!=hashmap[s[i]]:  #value 
        #             return False

        #     elif t[i] in hashset :
        #         return False
        #     hashmap[s[i]]=t[i]
        #     hashset.add(t[i])
        # return True 

        # hashmap={}
        # for i in range(0,len(s)):
        #     if s[i] in hashmap :
        #         if t[i]!=hashmap[s[i]]:
        #             return False
        #     elif t[i] in hashmap.values():
        #         return False

        #     hashmap[s[i]]=t[i]
        # return True


















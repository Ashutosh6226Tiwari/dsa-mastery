class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap={}
        hashset=set()
        for i in range (0, len (s)):
            if s[i] in hashmap :
                if t[i]!=hashmap[s[i]]:  #value 
                    return False

            elif t[i] in hashset :
                return False
            hashmap[s[i]]=t[i]
            hashset.add(t[i])


        return True 



        # hashmap={}
        # for i in range(0,len(s)):
        #     if s[i] in hashmap :
        #         if t[i]!=hashmap[s[i]]:
        #             return False
        #     elif t[i] in hashmap.values():
        #         return False

        #     hashmap[s[i]]=t[i]
            
        # return True





















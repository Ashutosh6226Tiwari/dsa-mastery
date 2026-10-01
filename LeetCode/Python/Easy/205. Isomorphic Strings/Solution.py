class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap={}
        for i in range(0,len(s)):
            if s[i] in hashmap :
                if t[i]!=hashmap[s[i]]:
                    return False
            elif t[i] in hashmap.values():
                return False

            hashmap[s[i]]=t[i]
            
        return True
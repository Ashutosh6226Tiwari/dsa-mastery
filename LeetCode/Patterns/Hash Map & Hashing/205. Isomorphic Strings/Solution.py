class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len (t):
            return False
        hashmap={}
        for i in range(0,len(s)):
            if s[i] in hashmap and t[i]!=hashmap[s[i]]:
                return False

            hashmap[s[i]]=t[i]
            
        return True
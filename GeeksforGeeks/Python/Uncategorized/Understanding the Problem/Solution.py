class Solution:
    def reverseString(self, s: str) -> str:
        
        return s[::-1]
        
        # if s == "" :
        #     return s
        
        # return self.reverseString(s[1:])+s[0]     tle error 
        
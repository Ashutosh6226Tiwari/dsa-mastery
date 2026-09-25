class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        left =0
        right= len(s)-1
        while left < right :
            if s[left]!=s[right]:
                return False 
            left+=1
            right-=1
        return True
        
        # n=str(x)
        # if (n[::-1]==n[::]):
        #     return True
        # return False 
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False 
        original= x
        reversed_num=0
        while x>0:
            n=x%10
            reversed_num=reversed_num*10+n
            x=x//10
        return reversed_num==original


# method->2
        # s=str(x)
        # left =0
        # right= len(s)-1
        # while left < right :
        #     if s[left]!=s[right]:
        #         return False 
        #     left+=1
        #     right-=1
        # return True
# method->3
        # n=str(x)
        # if (n[::-1]==n[::]):
        #     return True
        # return False 
        
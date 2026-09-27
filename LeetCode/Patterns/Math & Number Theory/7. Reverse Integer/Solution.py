class Solution:
    def reverse(self, x: int) -> int:
        min ,max =-2**31,2**31-1
        res=0
        sign= -1 if x<0 else 1
        x=abs(x)
        while x!=0:
            n=x%10
            res=res*10+n
            x=x//10
        res=res*sign
        if res<min or res >max:
            return 0
        return res





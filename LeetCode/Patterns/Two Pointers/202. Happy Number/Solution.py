class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num:int)->int:
            total =0
            while num>0:
                lastdigit = num%10 
                total = total + lastdigit **2
                num=num//10
            
            return total 

        seen= set()
        while n!=1 and n not in seen :
            seen.add(n)
            n=get_next(n)

        return n==1
                
        
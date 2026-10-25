class Solution:
    def myPow(self, x: float, n: int) -> float:

        # return x**n  

# time and space = O(n)

# <------------------------------------------------------>

        def power (x,n):
            if n ==0 :
                return 1

            temp =power(x,n//2)
            res = temp * temp

            if n%2==1 :
                res = res *x
            
            return res 

        if n<0 :
            return 1/power (x,-n)
        return power(x,n)
# <------------------------------------------------------>

# time complexity =O(n)






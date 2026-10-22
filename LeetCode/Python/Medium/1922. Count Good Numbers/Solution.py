class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = n//2
        odd = n//2
        mod=10**9+7

        if n%2!=0:
            even+=1


        return (pow(5,even , mod ) * pow(4,odd , mod))% mod
        
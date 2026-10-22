class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a

        return self.getSum(a ^ b, (a & b) << 1)






# x << n   # multiply by 2^n
# x >> n   # divide by 2^n


# 001 << 1 = 2
# 010 << 1 = 4
# 100 << 1 = 8
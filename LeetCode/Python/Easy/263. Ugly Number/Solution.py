class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # Divide out all factors of 2, 3, and 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1
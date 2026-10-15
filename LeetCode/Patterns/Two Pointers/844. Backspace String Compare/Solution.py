class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        i, j = n - 1, m - 1

       
        while i >= 0 or j >= 0:

            idx1 = self.validindex(s, i)
            idx2 = self.validindex(t, j)

   
            if idx1 < 0 and idx2 < 0:
                return True 

           
            if idx1 < 0 or idx2 < 0:
                return False

          
            if s[idx1] != t[idx2]:
                return False 

            i = idx1 - 1
            j = idx2 - 1

        return True 

    def validindex(self, s: str, i: int) -> int:
        back = 0
        while i >= 0:
            if s[i] == "#":
                back += 1
            elif back > 0:
                back -= 1
            else:
                break 
            i -= 1

        return i


        # Time Complexity: $O(N + M)$
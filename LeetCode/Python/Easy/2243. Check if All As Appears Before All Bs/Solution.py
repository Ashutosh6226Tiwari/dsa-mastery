class Solution:
    def checkString(self, s: str) -> bool:

        # return 'ba'not in s                     # tc= O(n) , sc = O(1)

        seenb = False 
        for char in s :
            if char == "b":
                seenb = True 
            elif char=="a" and seenb==True : 
                return False 
        return True 

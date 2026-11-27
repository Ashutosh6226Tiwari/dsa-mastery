class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0]*n for _ in range (n)]
        left , right = 0 , n -1 
        top , bottom = 0 , n-1
        val = 1

        while left<=right and top <= bottom :
            
            # for filling left to right 
            for c in range (left , right+1 ):
                mat[top][c]=val
                val+=1
            top+=1

            # for filling top to bottom 
            for r in range (top , bottom+1):
                mat[r][right]=val
                val+=1
            right-=1

            # for filling right to left 
            for c in range (right, left -1 , -1):
                mat[bottom][c]=val
                val+=1
            bottom -=1

            # for filling bottom to top 
            for r in range (bottom , top -1 ,-1):
                mat[r][left]=val
                val+=1
            left+=1

        return mat

# time complexity = O(n*2)
# space complexity = O(1)















        
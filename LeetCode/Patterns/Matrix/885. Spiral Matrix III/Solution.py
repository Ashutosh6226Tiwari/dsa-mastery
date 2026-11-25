class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        r,c = rStart , cStart 
        steps=1           #now of steps to take before turning 
        dir_idx=0         #start facing right 

        while len(res)< rows*cols:
            for _ in range (2):
                dr,dc=direction[dir_idx]
                for _ in range (steps):
                    if (0<=r<rows and 0<=c<cols):
                        res.append([r,c])
                    r,c = r+dr , c+dc
                dir_idx=(dir_idx+1)%4
            steps+=1

        return res

# time complexity = O(n*m)
# space complexity = O(1)       










        
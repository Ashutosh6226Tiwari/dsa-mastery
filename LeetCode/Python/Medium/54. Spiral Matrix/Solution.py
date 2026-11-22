class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        left , right = 0 , len(matrix[0])
        top , bottom = 0 , len(matrix)
            
        while left<right and top <bottom :
            for col in range (left , right ):
                res.append(matrix[top][col])
            top+=1

            for row in range (top , bottom):
                res.append(matrix[row][right-1])
            right-=1

            if top<bottom:
                for col in range (right-1 , left-1 ,-1 ):
                    res.append(matrix[bottom-1][col])
                bottom-=1

            if left< right :
                for row in range (bottom-1,top-1,-1):
                    res.append(matrix[row][left])
                left+=1
        
        return res 













        
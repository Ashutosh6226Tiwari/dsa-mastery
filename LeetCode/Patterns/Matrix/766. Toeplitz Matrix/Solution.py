class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for r in range (1 , len (matrix)):
            if matrix[r][1:] != matrix [r-1][:-1]:
                return False 
            
        return True 
        
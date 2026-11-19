class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:

        for r in range (1 , len (matrix)):
            if matrix[r][1:] != matrix [r-1][:-1]: 
                return False 
            
        return True 

# time complexity =O(n x M)
# space complexity= O(n)             it is for one pass .. one row at a time 
# <-------------------------------------------------------------------------------->

        # row= len(matrix)
        # cols= len(matrix[0])
        # for r in range (1 ,row):
        #     for c in range (1 , cols):
        #         if matrix[r][c] !=matrix[r-1][c-1]:
        #             return False 
        # return True 

# time complexity = O(m x n )
# space complexity = O(1)
        
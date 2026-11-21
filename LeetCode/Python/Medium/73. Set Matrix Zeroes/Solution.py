class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        row , cols = len(matrix), len(matrix[0])
        first_row = any(matrix[0][c]==0 for c in range (cols) )
        first_cols = any(matrix[r][0]==0 for r in range (row) )
# make first row and colmn to store the zero 
        for r in range (1,row):
            for c in range (1,cols):
                if matrix[r][c]==0 :
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range (1,row):
            for c in range (1 ,cols):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
# now zero out the first row and first colm if needed 
        if first_row:
            for c in range (cols):
                matrix[0][c]=0

        if first_cols:
            for r in range (row):
                matrix[r][0]=0

        

# time complexity = O(n*m)
# space complexity = O(1)

# <---------------------------------------------------------------------->
        # row , cols = len (matrix ) , len(matrix[0])
        # zero_row = set()
        # zero_cols = set()

        # for r in range (row):
        #     for c in range (cols):
        #         if matrix[r][c]==0:
        #             zero_row.add(r)
        #             zero_cols.add(c)

        # for r in range (row):
        #     for c in range(cols):
        #         if r in zero_row or c in zero_cols :
        #             matrix[r][c]=0

        

# time complexity = O(n*m)
# space complexity = O(m+n)


        
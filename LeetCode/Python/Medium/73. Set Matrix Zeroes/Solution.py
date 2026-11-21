class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row , cols = len (matrix ) , len(matrix[0])
        zero_row = set()
        zero_cols = set()

        for r in range (row):
            for c in range (cols):
                if matrix[r][c]==0:
                    zero_row.add(r)
                    zero_cols.add(c)

        for r in range (row):
            for c in range(cols):
                if r in zero_row or c in zero_cols :
                    matrix[r][c]=0

        return  matrix

        
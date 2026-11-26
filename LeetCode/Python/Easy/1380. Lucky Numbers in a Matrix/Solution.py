class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:

        # row_min= {min(row) for row in matrix }
        # col_max = {max(col) for col in zip (*matrix)}

        # return list(row_min & col_max)

# time complexity = o(n*m)
# space complexity = O(n+m)        

        rows , colm = len(matrix) , len (matrix[0])
        res = []

        row_min= set()
        for row in range (rows):
            row_min.add(min(matrix[row]))

        col_max=set()
        for col in range (colm):
            curr_max= matrix[0][col]
            for row in range (rows):
                curr_max= max(curr_max , matrix[row][col])
            col_max.add(curr_max)

        for n in row_min  :
            if n in col_max :
                res.append(n)
        return res










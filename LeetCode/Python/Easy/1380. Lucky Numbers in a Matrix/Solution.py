class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:

        row_min= {min(row) for row in matrix }
        col_max = {max(col) for col in zip (*matrix)}

        return list(row_min & col_max)

# time complexity = o(n*m)
# space complexity = O(n+m)        

        rows , colm = len(matrix) , len (matrix[0])
        res = []

        row_max= set()
        for row in range (rows):
            row_max.add(max(matrix[row]))

        col_max=set()
        for col in range (colm):
            curr_max= matrix[0][c]
            for row in ragne (rows):
                curr_max= max(curr_max , matrix[r][c])
            col_max.add(curr_max)

        for n in row_max :
            if n in col_max :
                res.append










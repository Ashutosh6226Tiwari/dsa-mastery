class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row = len(matrix)
        colm = len(matrix[0])

        res=[]
        for j in range (colm):
            sublist=[]
            for i in range (row):
                sublist.append(matrix[i][j])
            res.append(sublist)
    
        return res

        
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:

        # row = len(matrix)
        # colm = len(matrix[0])
        # res=[]
        # for c in range (colm):
        #     sublist=[]
        #     for r in range (row):
        #         sublist.append(matrix[r][c])
        #     res.append(sublist)
    
        # return res

# <--------------------------------------------------------------->
        # row = len(matrix)
        # colm = len(matrix[0])
        # res=[[0]*row for _ in range(colm)]

        # for r in range (row):
        #     for c in range (colm):
        #         res[c][r]=matrix[r][c]
        
        # return res
# <---------------------------------------------------------------------->

        # res=[[0 for _ in range (row)] for _ in range(colm)]

# <------------------------------------------------------------------------->

        return [list(colm)for colm in zip(*matrix)]


        
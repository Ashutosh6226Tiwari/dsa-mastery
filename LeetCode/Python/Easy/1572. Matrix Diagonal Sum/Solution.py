class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n=len(mat)
        total=0

        for i in range(n):
            total+=mat[i][i]

            if i != n-i-1:
                total+=mat[i][i]

        return total




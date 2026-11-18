class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:

        # n=len(mat)
        # total=0
        # for i in range(n):
        #     total+=mat[i][i]

        #     if i != n-i-1:
        #         total+=mat[i][i]

        # return total

# <------------------------------------------------------------>
        # n=len(mat)
        # total=0
        # for i in range (n):
        #     total+=mat[i][i]
        #     total+=mat[i][n-i-1]

        # if n%2==1:
        #     total-=mat[n//2][n//2]

        # return total

# <--------------------------------------------------------------------->
# by two pointer    
        # total = 0
        # left , right = 0 , len(mat)-1
        # for row in mat :
        #     if left ==right :
        #         total +=row[right]
        #     else :
        #         total += row[left]+row[right]
            
        #     left +=1
        #     right -=1
        # return total





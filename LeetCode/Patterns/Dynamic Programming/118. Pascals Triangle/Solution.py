class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if (numRows==1):
            return [[1]]        
        if (numRows==2):        
            return [[1],[1,1]]
        ans =[[1],[1,1]]
        for idx in range (3,numRows+1):
            current_list=[1]
            prev_list=ans[-1]
            for i in range (1,len(prev_list)):
                value =prev_list[i]+prev_list[i-1]
                current_list.append(value)
            current_list.append(1)
            ans.append(current_list)
        return ans    

                




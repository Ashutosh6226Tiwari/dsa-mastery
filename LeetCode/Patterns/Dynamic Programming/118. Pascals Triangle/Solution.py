class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans=[[1]]
        for _ in range (1,numRows):
            prev=ans[-1]
            row=[1]+[prev[i]+prev[i+1]for i in range (len(prev)-1)]+[1]
            ans.append(row)
        return ans


        # if (numRows==1):
        #     return [[1]]        
        # if (numRows==2):        
        #     return [[1],[1,1]]
        # ans =[[1],[1,1]]
        # for idx in range (2,numRows):
        #     current_list=[1]
        #     prev_list=ans[-1]
        #     for i in range (1,len(prev_list)):
        #         value =prev_list[i]+prev_list[i-1]
        #         current_list.append(value)
        #     current_list.append(1)
        #     ans.append(current_list)
        # return ans    
                                            
                



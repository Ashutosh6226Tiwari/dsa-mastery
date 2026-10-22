class Solution:
    def removeStars(self, s: str) -> str:
        s_list = list(s)
        write_idx=0
        for char in s_list:
            if char == '*':
                write_idx-=1    #back space 

            else :
                s_list[write_idx]=char   #over write 
                write_idx+=1             #next index

        return "".join(s_list[:write_idx])

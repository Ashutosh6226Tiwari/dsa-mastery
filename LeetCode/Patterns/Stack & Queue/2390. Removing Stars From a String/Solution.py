class Solution:
    def removeStars(self, s: str) -> str:
        s_list = list(s)
        write=0
        for curr in s_list:
            if curr == '*':
                write-=1

            else :
                s_list[write]=curr
                write+=1

        return "".join(s_list[:write])

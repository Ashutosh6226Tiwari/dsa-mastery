import math
class MinStack:
    def __init__(self):
        self.stack = []
        self.curr_min= math.inf

    def push(self, value: int) -> None:
        if self.curr_min > value :
            self.curr_min = value

        self.stack.append ((value , self.curr_min))

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack :
            self.curr_min = math.inf
        else :
            self.curr_min = self.stack[-1][1]        

    def top(self) -> int:
        return self.stack [-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]         


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




















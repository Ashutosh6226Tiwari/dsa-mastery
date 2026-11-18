class stack :
    def __init__ (self):
        self.stack =[]
    def push (self, data):
        self.stack.append(data)
    def pop (self):
        return self.stack.pop()
    def top (self):
        return self.stack[-1]  if stack else -1
    def isempty (self):
        return len(self.stack)==0

class MyQueue:

    def __init__(self):
        self.s1=stack()
        self.s2=stack()

    def push(self, x: int) -> None:
        while not self.s1.isempty():
            e1=self.s1.top()
            self.s1.pop()
            self.s2.push(e1)
        self.s1.push(x)
        
        while not self.s2.isempty():
            e1=self.s2.top()
            self.s2.pop()
            self.s1.push(e1)

    def pop(self) -> int:
        return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1.top()

    def empty(self) -> bool:
        return self.s1.isempty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



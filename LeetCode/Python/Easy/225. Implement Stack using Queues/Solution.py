class queue :
    def __init__(self):
        self.queue=[]
    def push (self,ele):
       return self.queue.append(ele)
    def pop (self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def isempty (self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)

class MyStack:

    def __init__(self):
        self.queue=queue()    

    def push(self, x: int) -> None:
        n=self.queue.size()
        self.queue.push(x)

        while n>0:
            e1=self.queue.front()
            self.queue.pop()
            self.queue.push(e1)
            n-=1

    def pop(self) -> int:
        return self.queue.pop()     

    def top(self) -> int:
        return self.queue.front()

    def empty(self) -> bool:
        return self.queue.isempty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()







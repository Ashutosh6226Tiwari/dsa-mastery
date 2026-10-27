class listnode:
    def __init__(self,value):
        self.value=value
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        curr=self.head 
        while curr and index>0:
            curr=curr.next
            index-=1
        if not curr:                    # curr == None
            return -1
        return curr.value  

    def addAtHead(self, val: int) -> None:
        node=listnode(val)

        node.next= self.head
        self.head=node  

    def addAtTail(self, val: int) -> None:
        node=listnode(val)
        prev, curr= None,self.head
        while curr :
            prev= curr
            curr=curr.next
        if prev==None:
            self.head=node
        else:
            prev.next=node
        
    def addAtIndex(self, index: int, val: int) -> None:
        node = listnode(val)
        if index==0:
            self.addAtHead(val)
            return 
        
        prev , curr = None  , self.head
        while curr and  index>0:
            prev=curr
            curr=curr.next
            index-=1
        if index > 0:
            return 

        node.next= curr
        prev.next= node 

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        
        if index==0:
            self.head=self.head.next
            return 

        prev , curr= self.head , self.head.next
        while curr and  index>1:
            prev= curr
            curr= curr.next
            index-=1
        if not curr:
            return 
     
        prev.next= curr.next
        del curr
        

    
           


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class node:
    def __init__(self, value ):
        self.value=value 
        self.next=None
        
class Solution:
    def getCount(self, head):
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        
        return length
        
        
        
        
        
        
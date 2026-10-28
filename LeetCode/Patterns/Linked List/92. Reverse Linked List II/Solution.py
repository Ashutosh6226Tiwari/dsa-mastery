# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if not head and left==right:
            return head 
        
        dummy=ListNode(0,head)
        prev=dummy 

        for _ in range (left-1):
            prev=prev.next

        curr=prev.next
        for _ in range (right-left):
            nex=curr.next
            curr.next=nex.next
            nex.next=prev.next
            prev.next=nex
        
        return dummy.next









        
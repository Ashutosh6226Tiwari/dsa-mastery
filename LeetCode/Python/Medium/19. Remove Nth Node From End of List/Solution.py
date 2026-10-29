# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def getsize(head):
    size=0
    curr=head
    while curr:
        size+=1
        curr=curr.next
    return size
    
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        size=getsize(head)
        start=size-n+1

        dummy=ListNode(-1)
        dummy.next=head
        head=dummy


        prev=curr=head

        while start>0 :
            prev=curr
            curr=curr.next
            start-=1

        prev.next=curr.next
        del curr

        return head.next






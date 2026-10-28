# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        headA=self.reverseList(head.next)
        prev,curr= None , headA
        while curr:
            prev= curr
            curr=curr.next
        
        prev.next=head
        head.next=None
        
        return headA
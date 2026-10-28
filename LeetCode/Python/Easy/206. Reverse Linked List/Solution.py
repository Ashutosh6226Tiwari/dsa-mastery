# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

# iterative                           tc = O(n)

        # curr=head
        # prev=None
        # while curr:
        #     temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr= temp 

        # return prev

# tail recursion                        tc=O(n^2)

        if not head or not head.next:
            return head
        headA=self.reverseList(head.next)

        head.next.next=head
        head.next=None

        return headA



# head recursion                          tc= O(n^2)

        # if not head or not head.next:
        #     return head
        # headA=self.reverseList(head.next)
        # prev,curr= None , headA
        # while curr:
        #     prev= curr
        #     curr=curr.next
        
        # prev.next=head
        # head.next=None
        
        # return headA
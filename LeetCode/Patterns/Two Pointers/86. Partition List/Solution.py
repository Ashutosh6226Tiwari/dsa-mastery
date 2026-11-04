# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:

        # dummy heads
        less_dummy = ListNode(0)
        great_dummy = ListNode(0)

        # tail pointer
        less= less_dummy 
        great= great_dummy 

        curr= head 
        while curr :
            if curr.val < x :
                less.next = curr
                less = less.next
            else :
                great.next = curr
                great = great.next

            curr=curr.next

        less.next= great_dummy.next 
        great.next= None

        return less_dummy.next





        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

# by dummy   tc = sc = O(n)
        dummy=ListNode(0,next= head)
        prev= dummy 

        while prev.next and prev.next.next :
            first=prev.next
            second=prev.next.next

            # rewiring 
            prev.next=second
            first.next=second.next
            second.next=first 
            
            prev= first
        
        return dummy.next


# <---------------------------------------------------------------->
# by recursion     tc =O(n)  and sc= O(n)

        # if not head or not head.next :
        #     return head 
        
        # first = head
        # second = head.next

        # first.next= self.swapPairs(second.next)
        # second.next= first

        # return second










        
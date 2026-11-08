# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        #base case 
        if not head or not head.next:
            return head
        
        #find mid 
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next

        #reveser second half
        prev= None 
        curr=slow.next
        slow.next=None
        while curr:
            tem= curr.next
            curr.next= prev
            prev= curr
            curr= tem 
        
        # merge (rewiering )
        first= head
        second = prev

        while second :
            tem1=first.next
            tem2=second.next

            first.next=second
            second.next=tem1

            first= tem1
            second= tem2














        
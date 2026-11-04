# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:

# wtc = O(n^2) and btc = O(n)  and st = O (1)

        if not head or not head.next:
            return head 

        dummy=ListNode(0, next= head)
        prev= dummy 
        last_sort= head
        curr=head.next
        while curr :
            if last_sort.val <= curr.val:
                last_sort = last_sort.next

            else :
                prev = dummy 
                while prev.next.val < curr.val :    
                    prev=prev.next

                last_sort.next=curr.next
                curr.next= prev.next
                prev.next= curr

            curr=last_sort.next

        return dummy.next





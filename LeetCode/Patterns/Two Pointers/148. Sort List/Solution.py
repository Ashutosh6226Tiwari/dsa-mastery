# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next :
            return head 

        mid=self.get_mid(head)
        left=head 
        right=mid.next
        mid.next=None

        left_sort=self.sortList(left)
        right_sort=self.sortList(right)

        return self.get_merge(left_sort , right_sort )
        
    def get_mid (self , head:ListNode)-> ListNode:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow 


    def get_merge (self, l1 : Optional [ListNode] , l2 : Optional [ListNode] )-> Optional [ListNode]:

        dummy=ListNode (0)
        curr=dummy 
        
        while l1 and  l2 :
            if l1.val <= l2.val:
                curr.next=l1
                l1=l1.next

            else :
                curr.next=l2
                l2=l2.next

            curr=curr.next

        curr.next= l1 if l1 else l2

        return dummy.next
                


















        
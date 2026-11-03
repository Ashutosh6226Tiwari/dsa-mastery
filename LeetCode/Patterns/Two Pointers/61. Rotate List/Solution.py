# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        #  edge case if list was empty list or single node or no rotation needed 
        if not head or not head.next or k==0:
            return head 
        
        # calculate the length of list 
        length=0 
        curr=head
        while curr :
            length+=1
            curr=curr.next

        # minimize the k 
        k=k%length 
        if k==0 :
            return head

        # advance fast pointer 
        fast=head
        for _ in range (k):
            fast=fast.next
        
        # move both slow and fast pointer till fast reachers the last node 
        slow = head
        while fast.next:
            slow=slow.next
            fast=fast.next

        # rewrite the pointer 
        new_head=slow.next
        fast.next=head
        slow.next=None

        return new_head


# time complexity = O(n)
# space complexity = O(1)







        
        





















# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        end = head
        n= k 
        while end and n>0:
            end=end.next
            n-=1
            
        if n!=0:
            return head 

        # revrse the current 
        curr , prev = head , None 
        while curr!=end :
            tem=curr.next
            curr.next= prev
            prev = curr
            curr = tem 

        
        head.next = self.reverseKGroup(end , k )
        return prev
        


        
        
















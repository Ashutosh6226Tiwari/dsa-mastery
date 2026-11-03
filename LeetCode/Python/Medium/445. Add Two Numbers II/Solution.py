# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # reverse in place
        def reverse_list (head : Optional [ListNode])-> Optional [ListNode]:
            prev=None
            curr=head
            while curr :
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev

        # reverse both list 
        l1 = reverse_list(l1)
        l2 = reverse_list(l2)
        #add and build the resul backward (prepand)

        carry=0
        head=None
        while l1 or l2 or carry :
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            total = val1 + val2 + carry 
            carry = total // 10     # to take second place element 
            
        # pre append directly to the front  
            new_node=ListNode(total % 10)
            new_node.next=head
            head = new_node 

            if l1 :
                l1=l1.next
            if l2 :
                l2=l2.next
                

        return head 
        










        
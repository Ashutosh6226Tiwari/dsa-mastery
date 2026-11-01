# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next :
            return True 

        #for finding mid 
        slow = fast = head 
        while fast.next and fast.next.next :
            slow= slow.next
            fast=fast.next.next 

        #for reversing 
        prev=None 
        curr=slow.next
        while curr :
            tem = curr.next
            curr.next= prev
            prev = curr
            curr= tem
        
        first_half = head
        second_half= prev
        is_pal= True 

        while is_pal and second_half :
            if first_half.val != second_half.val :
                is_pal = False

            first_half =  first_half.next
            second_half = second_half.next  

        return is_pal              






        
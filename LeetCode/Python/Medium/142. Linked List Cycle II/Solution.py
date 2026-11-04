# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # by slow and fast pointer   tc = O(n) and sc = O(1)

        slow = fast = head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast :
                slow = head 
                while slow != fast :
                    slow=slow.next 
                    fast=fast.next 
                return slow 
        return None


# <----------------------------------------------------------->
        # by hash set    tc = sc = O(n) 

        curr = head 
        visited=set()
        while curr :
            if curr in visited :
                return curr
            
            visited.add(curr)
            curr= curr.next 
        return None













        
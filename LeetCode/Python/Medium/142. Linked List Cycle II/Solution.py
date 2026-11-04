# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # by slow and fast pointer   tc = O(n)






# <----------------------------------------------------------->
        # by hash set    tc = O(n) and sc =O(n)

        curr = head 
        visited=set()
        while curr :
            if curr in visited :
                return curr
            
            visited.add(curr)
            curr= curr.next 
        return None













        
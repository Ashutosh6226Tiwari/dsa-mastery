# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # by slow and fast











        # by hashmap      tc=O(n)
        curr= head 
        hashmap = {}
        while curr :
            if curr in hashmap :
                return True 
            
            hashmap[curr]=True
            curr=curr.next
        return False 















         
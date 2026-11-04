# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # by slow and fast         tc = sc = O(n)

        slow = fast = head 
        while fast and fast.next :
            slow =slow.next               # move 1 step 
            fast = fast.next.next         # move 2 step 
            
            if slow == fast :             # both meet  
                return True 
        return False

# <---------------------------------------------------------------->
        # # by hashmap      tc=O(n) and sc=O(n)

        # curr= head 
        # hashmap = {}
        # while curr :
        #     if curr in hashmap :
        #         return True 
            
        #     hashmap[curr]=True
        #     curr=curr.next
        # return False 















         
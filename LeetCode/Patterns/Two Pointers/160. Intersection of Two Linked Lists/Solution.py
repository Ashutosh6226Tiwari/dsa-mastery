# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

#         #base case if nothing is there
#         if not headA or not headB :
#             return None
        
#         pA=headA
#         pB=headB

#         # Continue until both pointers meet (either at the intersection node or at None)

        
#         while pA != pB:
#             pA=pA.next if pA  else headB
#             pB=pB.next if pB else headA
        
#         return pA

# # by hashset

        pA=headA
        hashset=set()
        while pA :
            hashset.add(pA)
            pA=pA.next
        
        curr= headB
        while curr and curr not in hashset:
            curr=curr.next
        
        if curr:
            return curr
        return None 


# tc= O(n+m) and sc=O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the duplicate node
                curr.next = curr.next.next
            else:
                # Advance only when the next value is strictly different
                curr = curr.next

        return head
        
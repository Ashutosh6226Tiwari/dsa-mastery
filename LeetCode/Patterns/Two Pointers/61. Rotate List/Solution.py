# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Minimize k
        k = k % length
        if k == 0:
            return head

        # Step 3: Advance fast pointer k steps ahead
        fast = head
        for _ in range(k):
            fast = fast.next

        # Step 4: Move both fast and slow until fast reaches the last node
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Step 5: Rewire pointers
        new_head = slow.next
        fast.next = head
        slow.next = None

        return new_head
        
        





















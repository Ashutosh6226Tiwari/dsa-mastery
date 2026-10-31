# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# <--------------------------------------------/>
# def getsize(head):
#     size=0
#     curr=head
#     while curr:
#         size+=1
#         curr=curr.next
#     return size

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # size=getsize(head)
        # mid=-1
        # if size%2==0:
        #     mid=(size//2)+1
        # else:
        #     mid=(size+1)//2
        
        # curr=head
        # while mid>1:
        #     curr=curr.next
        #     mid-=1
        # return curr

# <-------------------------------------------------->
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow






        
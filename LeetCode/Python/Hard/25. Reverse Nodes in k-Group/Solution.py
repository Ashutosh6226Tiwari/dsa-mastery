# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

    # tc = O(n) and sc =O(n/k)
        end = head
        n= k                                            
        while end and n>0:
            end=end.next
            n-=1
            
        if n!=0:
            return head 

        # revrse the current 
        curr , prev = head , None 
        while curr!=end :
            tem=curr.next
            curr.next= prev
            prev = curr
            curr = tem 

        
        head.next = self.reverseKGroup(end , k )
        return prev
        
# <--------------------------------------------------------------------->
# iterative approach      tc = O(n) and sc = O(1)

    #     dummy = ListNode (0, next= head)
    #     group_prev =dummy 

    #     while True:
    #         kth=self.get_kth (group_prev , k)
    #         if not kth:
    #             break 
        
    #         end=kth.next

    #         curr=group_prev.next
    #         prev=end
    #         while curr !=end:
    #             tem=curr.next
    #             curr.next=prev
    #             prev=curr
    #             curr=tem 

    #         tem=group_prev.next
    #         group_prev.next=kth
    #         group_prev=tem
    #     return dummy.next 

    # def get_kth(self, curr:Optional [ListNode], k:int)->Optional[ListNode]:
    #     while  curr and k>0:
    #         curr=curr.next
    #         k-=1
    #     return curr
        
        
















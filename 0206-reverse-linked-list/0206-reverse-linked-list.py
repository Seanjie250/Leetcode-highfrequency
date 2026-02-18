# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy 
        if not head or not head.next:
            return head
        dummy.next = head
        cur = prev.next
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return prev.next
            

            

            


        
        




        
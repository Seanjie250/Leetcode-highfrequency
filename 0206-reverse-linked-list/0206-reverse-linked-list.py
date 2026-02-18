# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = prev.next
        while cur and cur.next:
            nxt = cur.next
            cur.next= nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next
            

            

            


        
        




        
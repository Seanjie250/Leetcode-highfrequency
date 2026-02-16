# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 , p2 = dummy1 , dummy2
        cur = head
        while cur:
            if cur.val >= x:
                p2.next = cur
                p2 = p2.next
            elif cur.val < x:
                p1.next = cur
                p1 = p1.next
            
            temp = cur.next
            cur.next = None
            cur = temp
        
        p1.next = dummy2.next

        return dummy1.next
        


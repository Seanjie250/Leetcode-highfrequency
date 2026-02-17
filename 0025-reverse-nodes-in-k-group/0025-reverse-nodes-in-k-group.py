# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        prev = dummy
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        if length < k:
            return head
        times = length // k
        for _ in range(times):
            cur = prev.next
            for _ in range(k - 1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            prev = cur
        return dummy.next
                
            
                


            

        

        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        c = head
        while c:
            n += 1
            c = c.next
        dummy = ListNode(0 , next = head)
        p0 = dummy
        cur = head
        while n >= k:
                n -= k
                pre = None
                start = cur
                for _ in range(k):
                    nxt = cur.next
                    cur.next =  pre
                    pre = cur
                    cur = nxt
                p0.next = pre
                start.next = cur
                p0 = start
        return dummy.next
            



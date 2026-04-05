# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        p1 = head
        n = 1
        while p1.next:
            n += 1
            p1= p1.next

        dummy = ListNode(-1 , next = head)
        p0 = dummy
        cur = head
        while n >= k:
            n -= k
            prv = None
            start = cur
            for _ in range(k):
                nxt = cur.next
                cur.next = prv
                prv = cur
                cur = nxt
            p0.next = prv
            start.next = cur
            p0 = start
        return dummy.next




        
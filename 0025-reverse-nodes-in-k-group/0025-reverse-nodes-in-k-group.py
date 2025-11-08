# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def checkifk(self,node,k):
        for _ in range(k):
            if not node:
                return False
            node = node.next
        return True


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        if not head:
            return None
        while self.checkifk(prev.next , k):
            cur = prev.next
            nxt = cur.next
            for _ in range(k - 1):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next
            prev = cur
        return dummy.next
        
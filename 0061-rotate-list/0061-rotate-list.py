# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getlength(self,head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = self.getlength(head)
        if count == 0 or not head:
            return None
        k = k % count
        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
        
        
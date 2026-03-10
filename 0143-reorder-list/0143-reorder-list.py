# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmid(self , head):
        slow , fast = head ,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverselist(self , head):
        dummy = ListNode(-1)
        cur = head
        while cur:
            nxt = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = nxt
        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.findmid(head)
        head2 = self.reverselist(mid)

        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2
        return head

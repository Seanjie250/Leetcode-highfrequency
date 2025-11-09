class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        cur = head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next != cur:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next
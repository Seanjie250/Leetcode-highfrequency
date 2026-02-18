# Definition for singly-linked list.

class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val
class Solution:
    def reverse(self ,node):
        dummy = ListNode(-1)
        dummy.next = node
        prev = dummy
        cur = prev.next
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        
        right = self.reverse(slow)
        left = head
        while right:
            if right.val != left.val:
                return False
            else:
                right = right.next
                left = left.next
        return True


        


        
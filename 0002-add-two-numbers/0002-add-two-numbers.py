# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 , p2 = l1 , l2
        dummy = ListNode(-1)
        p = dummy
        while p1 or p2 or carry:
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            carry = val // 10
            val = val % 10
            p.next = ListNode(val)
            p = p.next
        return dummy.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2
        while p1 or p2 or carry:
            val = 0
            if p1:
                val += p1.val 
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            val += carry
            carry = val // 10
            val = val % 10
            p.next = ListNode(val)
            p = p.next
        return dummy.next

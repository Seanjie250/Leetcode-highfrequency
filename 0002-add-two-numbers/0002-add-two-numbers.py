# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        num = 0
        p1 = l1
        p2 = l2
        carry = 0
        while p1 or p2 or carry:
            num = carry
            if p1:
                num += p1.val
                p1 = p1.next
            if p2:
                num += p2.val
                p2 = p2.next
            carry = num // 10
            node = ListNode(num % 10)
            p.next = node
            p = p.next
        return dummy.next
            
            
        
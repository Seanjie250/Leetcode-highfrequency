# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        p1 = headA
        while p1:
            seen.add(p1)
            p1 = p1.next
        p2 = headB
        while p2 not in seen and p2:
            p2 = p2.next
        return p2 if p2 else None
            

        
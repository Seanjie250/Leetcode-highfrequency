# Last updated: 5/15/2025, 1:24:59 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head,None)
    def reverse(self,cur:ListNode,pre:ListNode) -> ListNode:
        if cur == None:
            return pre
        tmp = cur.next
        cur.next = pre
        return self.reverse(tmp,cur)




        
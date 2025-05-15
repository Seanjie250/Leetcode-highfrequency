# Last updated: 5/15/2025, 2:18:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next and curr.next.next:
            tmp1 = curr.next
            tmp2 = curr.next.next.next

            curr.next = curr.next.next
            curr.next.next = tmp1
            tmp1.next = tmp2
            curr = curr.next.next
        return dummy.next





        
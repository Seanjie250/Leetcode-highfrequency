# Last updated: 5/15/2025, 1:18:39 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head
        while head and head.next:
            node_1 , node_2 = head , head.next
            prev.next = node_2
            node_1.next , node_2.next = node_2.next , node_1
            prev = node_1
            head = node_1.next
        return dummy.next

        
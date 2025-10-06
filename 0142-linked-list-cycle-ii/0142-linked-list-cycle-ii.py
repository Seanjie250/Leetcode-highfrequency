# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast , slow = head , head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            while slow == fast:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return  slow


        


        
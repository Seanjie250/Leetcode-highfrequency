# Last updated: 5/15/2025, 2:38:45 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = fast = dummy
        
        
        
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
            
        return dummy.next
        
        
        
        
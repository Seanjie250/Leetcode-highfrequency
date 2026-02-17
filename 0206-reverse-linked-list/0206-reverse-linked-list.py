# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not  head.next:
            return head
        dummy = ListNode(0, head)
        p  = head
        prev = dummy
        while p and p.next:
            nxt = p.next
            p.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return prev.next

            


        
        




        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 , number_2 = 0 , 0
        dummy_1 = ListNode(0)
        dummy_2 = ListNode(0)
        dummy_1.next = self.reverse(l1)
        dummy_2.next = self.reverse(l2)
        node_1 = dummy_1.next
        node_2 = dummy_2.next
        while node_1:
            number_1 = number_1 * 10 + node_1.val
            node_1 = node_1.next
        while node_2:
            number_2 = number_2 * 10 + node_2.val
            node_2 = node_2.next
        number_3 = number_1 + number_2
        answer = ListNode(0)
        current = answer
        if number_3 == 0:
            return ListNode(0)
        while number_3 > 0:
            digit = number_3 % 10
            current.next = ListNode(digit)
            number_3 = number_3 // 10
            current = current.next
        return answer.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        cur_1, cur_2 = list1, list2
        while cur_1 and cur_2:
            if cur_1.val >= cur_2.val:
                cur.next = cur_2
                cur_2 = cur_2.next
            elif cur_1.val < cur_2.val:
                cur.next = cur_1
                cur_1 = cur_1.next
            cur = cur.next
        if cur_1:
            cur.next = cur_1
            cur_1 = cur_1.next
            cur = cur.next
        if cur_2:
            cur.next = cur_2
            cur_2 = cur_2.next
            cur = cur.next
        return dummy.next
            



                

        

        

        
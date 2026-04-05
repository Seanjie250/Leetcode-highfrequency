# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        if not lists:
            return None
        for index , head in enumerate(lists):
            if head:
                val = head.val
                heapq.heappush(heap , (val , index, head))
        dummy = ListNode(-1)
        p = dummy
        while heap:
            val , index , node = heapq.heappop(heap)
            nxt = ListNode(val)
            p.next = nxt
            p = p.next
            if node.next:
                nxt_val = node.next.val
                heapq.heappush(heap , (nxt_val , index , node.next))
        return dummy.next

            
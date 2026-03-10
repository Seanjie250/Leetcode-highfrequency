# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy  = ListNode(-1)
        p = dummy
        heap = []
        for idx , head in enumerate(lists):
            if head:
                val = head.val
                heapq.heappush(heap , (val , idx , head))
        while heap:
            val , index , node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap , (node.next.val , index , node.next))
        return dummy.next




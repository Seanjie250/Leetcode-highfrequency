# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index , head in enumerate(lists):
            if head:
                val = head.val
                heapq.heappush(heap , (val , index , head))
        dummy = ListNode(-1)
        p = dummy
        while heap:
            val ,index, cur = heapq.heappop(heap)
            p.next = cur
            p = p.next
            if cur.next:
                heapq.heappush(heap , (cur.next.val , index,  cur.next))
        return dummy.next

        
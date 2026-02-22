# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i in range(len(lists)):
            head = lists[i]
            if head:
                val = head.val
                heapq.heappush(pq , (val , i , head))
        dummy = ListNode(-1)
        p = dummy
        while pq:
            val ,index , node = heapq.heappop(pq)
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val , index , node.next))
            p = p.next
        return dummy.next

        
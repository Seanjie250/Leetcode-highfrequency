# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        dummy = ListNode(-1)
        p = dummy
        for i in range(len(lists)):
            head = lists[i]
            if head:
                heapq.heappush(pq , (head.val , i , head))
        while pq:
            val , i , node = heapq.heappop(pq)
            p.next = node
            if node.next:
                new_node = node.next
                heapq.heappush(pq , (new_node.val, i , new_node))
            p = p.next
        return dummy.next

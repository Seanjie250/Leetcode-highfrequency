# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        dummy = ListNode(-1)
        p = dummy
        pq = []
        for i , node in enumerate(lists):
            if node is not None:
                heapq.heappush(pq, (node.val ,i, node))
        
        while pq:
            val , i , node = heapq.heappop(pq)
            if node.next is not None:
                heapq.heappush(pq, (node.next.val , i,node.next))
            p.next = node
            p = p.next
        
        return dummy.next

        
        
        
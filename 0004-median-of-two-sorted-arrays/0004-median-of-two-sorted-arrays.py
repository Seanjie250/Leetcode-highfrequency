class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_heap , min_heap = [] , []
        for num in nums1 + nums2:
            heapq.heappush(max_heap , - num)
            heapq.heappush(min_heap , -heapq.heappop(max_heap))

            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap , -heapq.heappop(min_heap))
            
        if len(min_heap) < len(max_heap):
            median = - max_heap[0]
            
        else:
            median = (min_heap[0] - max_heap[0]) / 2
        return median

            


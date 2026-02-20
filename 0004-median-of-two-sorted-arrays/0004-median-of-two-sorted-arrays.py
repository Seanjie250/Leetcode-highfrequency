class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_heap , min_heap = [] , []
        for num in nums1 + nums2:
            heapq.heappush(max_heap , - num)
            heapq.heappush(min_heap , -heapq.heappop(max_heap))

            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap , -heapq.heappop(min_heap))
            
        if len(max_heap) > len(min_heap):
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

            


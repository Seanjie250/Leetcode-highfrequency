class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals = sorted(intervals , key = lambda x : x[0])
        for start , end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap , end)
        return len(heap)
            

        
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        sort = sorted(intervals)
        for i in sort:
            if heap == [] or heap[0] > i[0]:
                heapq.heappush(heap , i[1])
            else:
                heapq.heapreplace(heap , i[1])
        return len(heap)
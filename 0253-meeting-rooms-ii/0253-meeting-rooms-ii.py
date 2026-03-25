class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        room = []
        res = 0
        for interval in intervals:
            if not room or room[0] > interval[0]:
                heapq.heappush(room , interval[1])
            else:
                while room and interval[0] >= room[0]:
                    heapq.heappop(room)
                heapq.heappush(room , interval[1])
            res = max(res , len(room))
        return res

                

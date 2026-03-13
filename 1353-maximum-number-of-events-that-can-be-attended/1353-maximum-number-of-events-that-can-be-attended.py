class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap = []
        events = sorted(events , key = lambda x:x[0])
        n = len(events)
        count = 0
        i = 0
        maxm = max(end for _ ,end in events)
        for day in range(1 , maxm + 1):
            while i < n and events[i][0] == day :
                heapq.heappush(heap , events[i][1])
                i += 1
               

            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                count += 1
            if count == n and not heap:
                break
        return count

        


        
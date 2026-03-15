class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v, w in times:
            graph[u].append((v , w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0 , k)]
        while heap:
            time , node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for v , w in graph[node]:
                if w + time < dist[v]:
                    dist[v] = w + time
                    heapq.heappush(heap , (dist[v] , v))
        print(dist)
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1


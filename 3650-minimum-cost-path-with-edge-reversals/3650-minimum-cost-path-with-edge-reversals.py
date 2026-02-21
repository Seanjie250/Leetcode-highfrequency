class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u , v ,  w in edges:
            adj[u].append((w , v))
            adj[v].append((2 * w , u))

        
        heap = [(0 , 0)]
        dic = [float('inf')] * n
        dic[0] = 0
        while heap:
            d , node = heapq.heappop(heap)
            if node == n - 1:
                return d
            if d != dic[node]:
                continue
            for w , v in adj[node]:
                if dic[node] + w < dic[v]:
                    dic[v] = dic[node] + w
                    heapq.heappush(heap , (dic[v] , v))
        return -1

        

        
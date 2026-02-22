class Solution:
    
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u , v , w in edges:
            graph[u].append((v , w))
            graph[v].append((u , 2 * w))
        
        dic = [float('inf')] * n
        dic[0] = 0
        pq = [(0 , 0)]
        while pq:
            cost , node = heapq.heappop(pq)
            if node == n - 1:
                return cost
           
            if cost != dic[node]:
                continue
            for v , w in graph[node]:
                if cost + w < dic[v]:
                    dic[v] = cost + w
                    heapq.heappush(pq , (dic[v] , v))
        
        return -1

        


        
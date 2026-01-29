class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i] , profits[i]) for i in range(n)]
        projects.sort()
        maxheap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <=w:
                heapq.heappush(maxheap , -projects[i][1])
                i += 1
            if not maxheap:
                break
            w -= heapq.heappop(maxheap)
        return w
            
            

            




            

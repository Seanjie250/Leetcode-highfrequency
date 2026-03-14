class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        q = deque([i for i in range(n) if degree[i] == 1])

        remaining = n
        while q:
            if remaining <= 2:
                return list(q)
            remaining -= len(q)
            for i in range(len(q)):
                cur = q.popleft()
                for node in graph[cur]:
                    degree[node] -= 1
                    if degree[node] == 1:
                        q.append(node)

        return list(q)

        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph : Dict[str , list[tuple[str,float]]] = defaultdict(list)
        for (m , n) , val in zip(equations , values):
            graph[m].append((n , val))
            graph[n].append((m , 1.0 / val))

        def dfs(src , dst):
            if dst not in graph or src not in graph:
                return -1
            if src == dst:
                return 1
            visited = set()
            stack = [(src , 1.0)]
            visited.add(src)

            while stack:
                node , val = stack.pop()
                if node == dst:
                    return val
                for nei , value in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append((nei , val * value))
            return - 1
        return [dfs(a , b ) for a , b in queries]
                

        
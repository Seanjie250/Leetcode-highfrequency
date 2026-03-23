class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        degree = [0] * numCourses
        for c , p in prerequisites:
            graph[p].append(c)
            degree[c] += 1
        q = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        count = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                count += 1
                for co in graph[cur]:
                    degree[co] -= 1
                    if degree[co] == 0:
                        q.append(co)
        print(count)
        return count == numCourses


        
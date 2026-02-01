class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for course , pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1
        
        q = deque([i for i in range(numCourses) if degree[i] == 0])

        count = 0

        while q:
            cur = q.popleft()
            count += 1
            for course in graph[cur]:
                degree[course] -= 1
                if degree[course] == 0:
                    q.append(course)
        return count == numCourses
                




        
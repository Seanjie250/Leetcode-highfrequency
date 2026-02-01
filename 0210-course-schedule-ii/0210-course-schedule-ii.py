class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for course , pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1
        
        q = deque([i for i in range(numCourses) if degree[i] == 0])
        
        rst = []

        while q:
            cur = q.popleft()
            rst.append(cur)

            for course in graph[cur]:
                degree[course] -= 1
                if degree[course] == 0:
                    q.append(course)

        return rst if len(rst) == numCourses else []
        


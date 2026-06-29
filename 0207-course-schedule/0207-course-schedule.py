class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for course , pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1
        print(graph)
        print(degree)

        queue = deque()
        count = 0

        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        if not queue:
            return False
        while queue:
            for i in range(len(queue)):
                cur_course = queue.popleft()
                for course in graph[cur_course]:
                    degree[course] -= 1
                    if degree[course] == 0:
                        queue.append(course)
                count += 1

            
        return count == numCourses
        
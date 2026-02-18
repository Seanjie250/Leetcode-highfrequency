class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        graph = defaultdict(list)
        for course , prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degree[course] += 1
        
        q = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        count = 0
        while q:
            course = q.popleft()
            print(course)
            for c in graph[course]:
                degree[c] -= 1
                if degree[c] == 0:
                    q.append(c)
            count += 1

                    
        return True if count == numCourses else False
            
            
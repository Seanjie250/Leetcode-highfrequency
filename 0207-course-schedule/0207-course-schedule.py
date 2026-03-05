class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course , prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        count = 0

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
            
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                count += 1
                for course in graph[cur]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        q.append(course)
        return count == numCourses

        
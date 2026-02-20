class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses
        graph = defaultdict(list)
        for course , prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1
        print(graph)

        q = deque()

        for i in range(len(degrees)):
            if degrees[i] == 0:
                q.append(i)
        count = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                
                for courses in graph[cur]:
                    degrees[courses] -= 1
                    if degrees[courses] == 0:
                        q.append(courses)
                count += 1
        return count == numCourses





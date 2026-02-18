class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        graph = defaultdict(list)
        q = deque()
        rst = []
        for course , prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degree[course] += 1
        
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            cour = q.popleft()
            print(cour)
            for c in graph[cour]:
                degree[c] -= 1
                if degree[c] == 0:
                    q.append(c)
            
            rst.append(cour)
        return rst if len(rst) == numCourses else []

        
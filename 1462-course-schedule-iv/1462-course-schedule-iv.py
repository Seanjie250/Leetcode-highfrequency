class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
        rst = [False] * len(queries) 
        for i in range(len(queries)):
            query = queries[i]
            prerequeisite , course = query[0] , query[1]
            q = deque()
            visited = set()
            if not graph[prerequeisite]:
                continue
            else:
                for c in graph[prerequeisite]:
                    q.append(c)
                while q:
                    cur = q.popleft()
                    visited.add(cur)
                    if cur == course:
                        rst[i] = True
                        break
                    else:
                        if graph[cur]:
                            for c2 in graph[cur]:
                                if c2 not in visited:
                                    q.append(c2)
        return rst

            
            

        




class Solution:        
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        distict = set()
        def dfs(i , j , originalX , originalY , coordinate):
            if 0<= i < m and 0<= j < n and grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                coordinate.append((originalX - i , originalY - j))
                
                dfs(i + 1 , j , originalX , originalY , coordinate)
                dfs(i - 1 , j , originalX , originalY , coordinate)
                dfs(i , j + 1 , originalX , originalY , coordinate)
                dfs(i , j - 1 , originalX , originalY , coordinate)
            return coordinate
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    coordinate = []
                    shape = dfs(i , j , i , j , coordinate)
                    count += 1
                    distict.add(tuple(sorted(coordinate)))
        return len(distict)

        
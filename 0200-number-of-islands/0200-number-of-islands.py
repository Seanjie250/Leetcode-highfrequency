class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        count = 0
        visited = [[False] * n for _ in range(m)]
        def dfs(i , j):
            if not( 0<= i < m and 0<= j < n and not visited[i][j] and grid[i][j] == '1'):
                return 
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
           
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i , j)
        return count 

        
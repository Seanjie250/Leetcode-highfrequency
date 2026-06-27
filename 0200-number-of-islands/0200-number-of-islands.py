class Solution:
    directions = [[1,0] , [-1 , 0] , [0 , 1] , [0 , -1]]
    def dfs(self , grid,  visited , x , y):
        m , n = len(grid) , len(grid[0])
        for i , j in self.directions:
            dx = x + i
            dy = y + j
            if dx >= 0 and dx < m and dy >= 0 and dy < n and not visited[dx][dy] and grid[dx][dy] == '1':
                visited[dx][dy] = True
                self.dfs(grid , visited , dx , dy)
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    self.dfs(grid , visited , i , j)
                    count += 1
        return count


        
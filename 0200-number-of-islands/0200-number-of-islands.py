
class Solution:
    directions = [[1,0] , [-1,0] , [0,1] , [0,-1]]
    def dfs(self,grid, visited, x, y):
        if x >= len(grid) or x < 0 or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == '0':
            return 
        visited[x][y] = True
        for dx , dy in self.directions:
            self.dfs(grid,visited,dx + x,dy + y)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m , n = len(grid) , len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    
                    self.dfs(grid, visited, i , j )
                    count += 1
        return count
        
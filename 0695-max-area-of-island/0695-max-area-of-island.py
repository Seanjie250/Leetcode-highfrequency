class Solution:
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    def dfs(self,grid,visited,x,y):
        count = 1
        for i,j in self.direction:
            next_x = x + i
            next_y = y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            else:
                if not visited[next_x][next_y] and grid[next_x][next_y] == 1 :
                    visited[next_x][next_y] = True
                    count += self.dfs(grid,visited,next_x,next_y)
        return count

        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid) ,len(grid[0])
        rst = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    count = self.dfs(grid,visited,i,j)
                    rst = max(rst,count)
        return rst
        
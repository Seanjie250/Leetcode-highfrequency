class Solution:
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    def dfs(self,x,y,grid,visited):
        for m,n in self.direction:
            next_x = x + m
            next_y = y + n
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            else:
                if grid[next_x][next_y] == 1 and  not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    self.dfs(next_x,next_y,grid,visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        rst = 0
        grid = [list(map(int, row)) for row in grid]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    rst += 1
                    visited[i][j] = True
                    self.dfs(i,j,grid,visited)
        return rst







        
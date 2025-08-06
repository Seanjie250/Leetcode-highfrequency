class Solution:
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  


    def dfs(self,grid,visited,x,y):
        for i,j in self.direction:
            next_x = x + i
            next_y = y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            else:
                if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                    visited[next_x][next_y] = True
                    self.dfs(grid,visited,next_x,next_y)


    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * (len(grid[0])) for _ in range(len(grid))]
        rst = 0 
        grid = [list(map(int, row)) for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    rst += 1
                    visited[i][j] = True
                    
                    self.dfs(grid,visited,i,j)
        return rst





        
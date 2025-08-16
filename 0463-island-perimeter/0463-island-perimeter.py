class Solution:
    directions = [(1,0),(0,1),(0,-1),(-1,0)]
    def dfs(self,grid,x,y,visited):
        for i,j in self.directions:
            next_x = x + i
            next_y = y + j
            while 0<= next_x < len(grid) and 0<= next_y < len(grid[0]) and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                self.dfs(grid,next_x,next_y,visited)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r , c = len(grid),len(grid[0])
        visited = [[False] * c for _ in range(r)]
        perimeter = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    self.dfs(grid,i,j,visited)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter




                    

 

        
directions = [[1,0] , [-1,0] ,[0,1] , [0,-1]]
class Solution:
    def dfs(self,grid,visited , x , y ):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == '0':
            return
        visited[x][y] = True
        for dx , dy in directions:
            self.dfs(grid, visited , x + dx , y + dy)
    def numIslands(self, grid: List[List[str]]) -> int:
        row , col = len(grid) , len(grid[0])
        visited = [[False  for _ in range(col)] for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid , visited ,i , j)
                    count += 1
        return count
                


        
        
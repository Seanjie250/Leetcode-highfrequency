class Solution:
    directions = [[-1 , 0] , [0 , 1] , [0 , -1] , [1 , 0]]
    def dfs(self , grid, visited , i , j):
        m , n = len(grid) , len(grid[0])
        visited[i][j] = True
        for dx , dy in self.directions:
            new_x = i + dx
            new_y = j + dy
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1" and not visited[new_x][new_y]:
                self.dfs(grid , visited , new_x , new_y)

    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        count = 0
        visited = [[False]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    self.dfs(grid , visited , i , j)
        return count


        
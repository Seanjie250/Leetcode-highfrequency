class Solution:
    directions = [[1, 0] , [-1 , 0] , [0 , 1], [0 , -1]]
    def dfs(self , grid , visited , i , j):
        m , n = len(grid) , len(grid[0])
        visited[i][j] = True
        for dx , dy in self.directions:
            new_x , new_y = dx + i , dy + j
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                self.dfs(grid, visited , new_x , new_y)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    
                    self.dfs(grid , visited , i , j)
                    count += 1
        return count

        
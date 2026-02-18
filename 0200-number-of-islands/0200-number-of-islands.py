class Solution:
    directions = [[1, 0] , [0, 1] , [-1 , 0] , [0, -1]]
    def dfs(self, grid, visited , i , j):
        visited[i][j] = True
        for dx , dy in self.directions:
            new_x = dx + i
            new_y = dy + j
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and  not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                self.dfs(grid , visited , new_x , new_y)
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid , visited , i , j)
                    count += 1
        return count

        
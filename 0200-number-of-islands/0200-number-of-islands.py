class Solution:
    direction = [[-1 , 0] , [1 , 0] , [0 , 1] , [0 , -1]]
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        visited  = [[False] * n for _ in range(m)]
        def dfs(i , j):
            visited[i][j] = True
            for dx , dy in self.direction:
                new_x = dx + i
                new_y = dy + j
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                    dfs(new_x , new_y)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i , j)
                    count += 1
        return count


        
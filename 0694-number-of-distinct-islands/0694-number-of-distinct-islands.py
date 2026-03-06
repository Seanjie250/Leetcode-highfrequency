class Solution:
    directions = [[1,0] , [-1,0] , [0,1] , [0,-1]]
    def dfs(self, grid, visited , i , j , originali , originalj , path):
        visited[i][j] = True
        path.append((i - originali,j - originalj))
        m , n = len(grid) , len(grid[0])
        for dx , dy in self.directions:
            nx ,ny = i + dx , j + dy
            if 0<= nx < m and 0<= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                
                self.dfs(grid, visited , nx, ny , originali , originalj , path)
        return path
        

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    island_shape = self.dfs(grid, visited , i , j ,i , j ,[])
                    if island_shape:
                        print(island_shape)
                        seen.add(tuple(island_shape))
        return len(seen)

        
class Solution:
    directions = [(1,0),(0,1),(0,-1),(-1,0)]

    def dfs(self,grid,x,y,visited,key):
        visited[x][y] = True
        count = 1
        grid[x][y] = key
        for i,j in self.directions:
            next_x = x + i
            next_y = y + j
            if 0<= next_x < len(grid) and 0 <= next_y < len(grid) and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                count += self.dfs(grid,next_x,next_y,visited,key)
        return count
    def largestIsland(self, grid: List[List[int]]) -> int:
        area = defaultdict(int)
        key = 1
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area[key] = self.dfs(grid,i,j,visited,key)
                    key += 1
        rst = 0 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_island = 1
                    v = set()
                    for m,mn in self.directions:
                        next_x = i +  m
                        next_y = j + mn
                        if 0<= next_x < n and 0<= next_y < n and grid[next_x][next_y] != 0  and grid[next_x][next_y] not in v:
                            max_island += area[grid[next_x][next_y]]
                            v.add(grid[next_x][next_y])
                    rst = max(rst,max_island)
        if rst == 0:
            return n*n
        return rst

                    





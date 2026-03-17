class Solution:
    directions = [[-1 , 0] , [1, 0] , [0 , 1] , [0 , -1]]
    def largestIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        def dfs(i , j , island_id):
            count = 1
            m , n = len(grid) , len(grid[0])
            grid[i][j] = island_id
            for dx , dy in self.directions:
                new_x = i + dx
                new_y = j + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    count += dfs(new_x , new_y , island_id)
            return count
        
        island_id = 2
        size = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(i , j , island_id)
                    size[island_id] = count
                    
                    island_id += 1
        ans = float('-inf')
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    visited = set()
                    for dx , dy in self.directions:
                        new_x = i + dx
                        new_y = j + dy
                        if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] not in visited and  grid[new_x][new_y] > 1:
                            area += size[grid[new_x][new_y]]
                            visited.add(grid[new_x][new_y])
                    ans = max(ans , area)
        return ans if ans != float('-inf') else m * n

        



        
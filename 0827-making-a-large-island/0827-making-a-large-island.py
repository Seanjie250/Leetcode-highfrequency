class Solution:
    directions = [[1 , 0] , [-1, 0] , [0 , -1], [0 , 1]]
    def dfs(self , grid , i , j , island_id , area):
        grid[i][j] = island_id 
        m , n = len(grid) , len(grid[0])
        for dx , dy in self.directions:
            new_x = dx + i 
            new_y = dy + j
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                area += 1
                area = self.dfs(grid , new_x , new_y ,island_id , area)
        return area

    def largestIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        maxm = float('-inf')
        count = 1
        island_id = 2
        island_area = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 1
                    island_area[island_id] = self.dfs(grid ,  i , j , island_id, area)
                    island_id += 1
        maxm = max(island_area.values(), default=0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    a = 1
                    for dx , dy in self.directions:
                        new_x = dx + i 
                        new_y = dy + j
                        if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] > 1 and grid[new_x][new_y] not in seen:
                            a += island_area[grid[new_x][new_y]]
                            print(a)
                            seen.add(grid[new_x][new_y])
                    maxm = max(maxm , a)
                
        return maxm

        
class Solution:
    directions = [[1,0] , [-1 , 0] , [0, 1] , [0 , -1]]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()
        number = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i , j))
                    visited[i][j] = True
                if grid[i][j] == 1:
                    number += 1
        if number == 0:
            return 0
        times = 0
        count = 0
        while q:
            rottened = 0
            for i in range(len(q)):
                x, y = q.popleft()
                for dx , dy in self.directions:
                    new_x = dx + x
                    new_y = dy + y
                    if new_x < m and new_x >= 0 and new_y >= 0 and new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                        count += 1
                        rottened += 1
                        visited[new_x][new_y] = True
                        grid[new_x][new_y] = 2
                        q.append((new_x , new_y))
            if rottened > 0:
                times += 1 

        return times if count == number else -1
                    
                        
                    


        
class Solution:
    
    directions = [[1, 0] , [-1 , 0] ,[0 , 1] , [0 , -1]]
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m , n = len(grid) , len(grid[0])
        q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        fre = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i , j])
                    visited[i][j] = True
                if grid[i][j] == 1:
                    fre += 1
        if fre == 0:
            return 0
        count = 0
        rotten = 0
        while q:
            for i in range(len(q)):
                x , y = q.popleft()
                for dx , dy in self.directions:
                    new_x , new_y = x + dx , y + dy
                    if new_x >= m or new_x < 0 or new_y >= n or new_y < 0:
                        continue
                    if grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                        grid[new_x][new_y] = 2 
                        visited[new_x][new_y] = True
                        q.append([new_x , new_y])
                        rotten += 1

            count += 1

        
        
        return count - 1 if rotten == fre else -1
        
            

        
                
        




        
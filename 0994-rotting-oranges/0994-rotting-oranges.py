class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0] , [-1 , 0], [0, - 1], [0, 1]]
        count = 0
        q = deque()
       
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i , j))
                    visited[i][j] = True
                if grid[i][j] == 1:
                    count += 1
        rotten = 0
        times = 0
        while not q and count == 0:
            return 0
        while not q and count != 0:
            return -1
        while q:
            times += 1
            for _ in range(len(q)):
                i , j = q.popleft()
                for dx , dy in directions:
                    new_x = i + dx 
                    new_y = j + dy
                    if 0<= new_x < m and 0<= new_y < n and grid[new_x][new_y] == 1 and not visited[new_x][new_y] :
                        visited[new_x][new_y] = True
                        grid[new_x][new_y] == 2
                        rotten += 1
                        q.append((new_x , new_y))
            

        return times - 1 if rotten == count else -1


        
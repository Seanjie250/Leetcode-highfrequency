class Solution:
    directions = [[1, 0] , [-1 , 0] , [0 , 1] , [0, -1]]
    def dfs(self , board,  visited , word , x , y):
        m , n = len(board) , len(board[0])
        if len(word) == 0:
            return True
        for i , j in self.directions:
            dx = x + i 
            dy = y + j
            if dx >= 0 and dx < m and dy >= 0 and dy < n and board[dx][dy] == word[0] and not visited[dx][dy]:
                visited[dx][dy] = True
                if self.dfs(board, visited , word[1:] , dx , dy):
                    return True
                visited[dx][dy] = False
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board) , len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and not visited[i][j]:
                    visited[i][j] = True
                    if self.dfs(board , visited , word[1:] , i , j):
                        return True
                    visited[i][j] = False
        return False
        
        
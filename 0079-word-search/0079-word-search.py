class Solution:
    directions = [[-1 , 0] , [1 , 0] , [0 , -1] , [0 , 1]]
    def dfs(self , board , visited , word , i , j):
        print(word)
        if not word:
            return True
        m , n = len(board) , len(board[0])
        for dx , dy in self.directions:
            nx = dx + i
            ny = dy + j
            if 0 <= nx <  m and 0 <= ny < n and board[nx][ny] == word[0] and not visited[nx][ny]:
                visited[nx][ny] = True 
                if self.dfs(board,  visited , word[1:] , nx , ny):
                    return True
                visited[nx][ny] = False
        
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

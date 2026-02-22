class Solution:
    directions = [[0,1] , [0 , -1] , [1, 0] , [-1 , 0]]
    def dfs(self , board , visited , word , i , j):
        
        if not word:
            return True
        m ,n = len(board) , len(board[0])
        for dx , dy in self.directions:
            new_x , new_y = dx + i , dy + j
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == word[0]:
                visited[new_x][new_y] = True
                if self.dfs(board , visited , word[1:] , new_x , new_y):
                    return True
                visited[new_x][new_y] = False
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        m ,n = len(board) , len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(board , visited , word[1:], i , j):
                        return True
                    visited[i][j] = False
        return False
                    

        
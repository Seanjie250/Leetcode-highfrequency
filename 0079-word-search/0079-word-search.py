class Solution:
    directions = [[1, 0] , [-1 , 0] , [0 , -1], [0 , 1]]
    def dfs(self , board , visited , i , j , word):
        m , n = len(board) , len(board[0])
        if not word:
            return True
        for dx , dy in self.directions:
            new_x , new_y = i + dx , j + dy
            if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == word[0]:
                visited[new_x][new_y] = True
                if self.dfs(board , visited , new_x , new_y , word[1:]):
                    return True
                visited[new_x][new_y] = False
        return False
                   

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board) , len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and not visited[i][j]:
                    visited[i][j] = True
                    if self.dfs(board, visited, i , j ,word[1:]):
                        return True
                    visited[i][j] = False
        return False

        
        
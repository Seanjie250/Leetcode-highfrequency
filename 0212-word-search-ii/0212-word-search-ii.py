class Solution:
    directions = [[1, 0] , [0 , 1] , [0, - 1] , [-1 , 0]]
    def dfs(self, board, word , visited , i , j):
        m , n = len(board) , len(board[0])
        if len(word) == 0:
            return True
        for dx,dy in self.directions:
            new_x = dx + i
            new_y = dy + j
            if 0<= new_x < m and 0<= new_y < n and board[new_x][new_y] == word[0] and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                if self.dfs(board, word[1:] , visited , new_x , new_y):
                    return True
                visited[new_x][new_y] = False
        return False
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rst = []
        m , n = len(board) , len(board[0])
        for word in words:
            visited = [[False] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0] and not visited[i][j]:
                        visited[i][j] = True
                        if self.dfs(board , word[1:], visited , i , j):
                            if word not in rst:
                                rst.append(word)
                        visited[i][j] = False
        return rst



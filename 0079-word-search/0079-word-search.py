class Solution:
    directions = [[0,1] , [0 , -1] , [1, 0] , [-1 , 0]]
    def dfs(self, board , visited , i ,j ,word ,count):
        if board[i][j] != word[count]:
            return False
        if count == len(word) - 1:
            return True
        visited[i][j] = True
        m , n = len(board) , len(board[0])
        for dx , dy in self.directions:
            new_x = i + dx
            new_y = j + dy
            if new_x < m and new_x >= 0 and new_y >= 0 and new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == word[count + 1]:
                if self.dfs(board , visited , new_x ,new_y ,word ,count + 1):
                    return True
        visited[i][j] = False     
        return False
                
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        length = len(word)
        m , n = len(board) , len(board[0])
        ans = False
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board , visited , i ,j ,word,0):
                        return True
        return False
                   

                
                    
        


        
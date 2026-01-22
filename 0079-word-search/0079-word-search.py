class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = []

        visited = [[False] * n for _ in range(m)]

        def dfs(i,j,start):
            if start == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j]:
                return False
            if board[i][j] != word[start]:
                return False
            visited[i][j] = True
            found = (
                dfs(i + 1,j,start + 1) or 
                dfs(i - 1,j,start + 1) or 
                dfs(i,j - 1,start + 1) or 
                dfs(i,j + 1,start + 1)
            )
            visited[i][j] = False
            return found
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

                



        
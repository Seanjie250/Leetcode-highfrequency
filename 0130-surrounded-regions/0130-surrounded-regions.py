from collections import deque
class Solution:
    def bfs(self,board,x,y):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        board[x][y] = "W"
        q = deque()
        q.append((x,y))
        while q:
            r,c = q.popleft()
            for x , y in directions:
                next_x = r + x
                next_y = c + y
                if next_x >= len(board) or next_x < 0 or next_y >= len(board[0]) or next_y < 0:
                    continue
                if board[next_x][next_y] == "O":
                    q.append((next_x,next_y))
                    board[next_x][next_y] = "W"
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m ,n = len(board) , len(board[0])
        # check left and right side
        for i in range(m):
            if board[i][0] == "O":
                self.bfs(board,i,0)
            if board[i][n - 1] == "O":
                self.bfs(board,i,n - 1)
        #check top and bottom side
        for i in range(n):
            if board[0][i] == "O":
                self.bfs(board,0,i)
            if board[m - 1][i] == "O":
                self.bfs(board,m - 1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "W":
                    board[i][j] = "O"

        
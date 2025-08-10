class Solution:
    def dfs(self,board,x,y):
        board[x][y] = "W"
        direction = [[0,1] , [0,-1], [1,0] , [-1,0]]
        for di in direction:
            next_x = x + di[0]
            next_y = y + di[1]
            if next_x < 0 or next_x >= len(board) or next_y < 0 or next_y >= len(board[0]):
                continue
            if board[next_x][next_y] != "O" :
                continue
            self.dfs(board,next_x,next_y)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m ,n = len(board) , len(board[0])
        # check left and right side
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(board,i,0)
            if board[i][n - 1] == "O":
                self.dfs(board,i,n - 1)
        #check top and bottom side
        for i in range(n):
            if board[0][i] == "O":
                self.dfs(board,0,i)
            if board[m - 1][i] == "O":
                self.dfs(board,m - 1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "W":
                    board[i][j] = "O"

        
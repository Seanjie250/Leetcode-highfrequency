class Solution:
    def count(self, board, x, y, cont_live):
        directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
        ]
        rows, cols = len(board), len(board[0])
        
        live_count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 1:
                live_count += 1

        cont_live[(x, y)] = live_count

    def gameOfLife(self, board: List[List[int]]) -> None:
        row = len(board)
        col = len(board[0])
        cont_live = {}
        for i in range(row):
            for j in range(col):
                self.count(board, i ,j , cont_live)
        next_state = [[board[i][j] for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                live_neighbors = cont_live.get((i, j), 0)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    next_state[i][j] = 0
                elif board[i][j] == 0 and live_neighbors == 3:
                    next_state[i][j] = 1
        
        
        for i in range(row):
            for j in range(col):
                board[i][j] = next_state[i][j] 

                




        
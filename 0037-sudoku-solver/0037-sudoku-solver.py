class Solution:            
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]
        for i in range(9):
            for j in  range(9):
                num = board[i][j]
                if num != '.':
                    row_used[i].add(num)
                    col_used[j].add(num)
                    box_used[(i//3) * 3 + j//3].add(num)
        self.backtracking(
            board,
            row_used,
            col_used,
            box_used,
            0,0
        )
    def backtracking(self, board,
            row_used,
            col_used,
            box_used,row,col):
            if row == 9:
                return True
            next_row ,next_col = (row,col + 1) if col < 8 else (row + 1,0)
            if board[row][col] != '.':
                return self.backtracking(board,row_used,col_used,box_used,next_row,next_col)
            
            for num in map(str,range(1,10)):
                if (
                    num not in row_used[row] and 
                    num not in col_used[col] and 
                    num not in box_used[(row//3) * 3 + col//3]):
                    board[row][col] = num
                    row_used[row].add(num)
                    col_used[col].add(num)
                    box_used[(row//3) * 3 + col//3].add(num)
                    if self.backtracking(board,row_used,col_used,box_used,next_row,next_col):
                        return True
                    board[row][col] = '.'
                    row_used[row].remove(num)
                    col_used[col].remove(num)
                    box_used[(row//3) * 3 + col//3].remove(num)

            return False





        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sub = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    val = int(board[i][j])
                    box = (i // 3) * 3 + (j // 3)
                    if row[i][val - 1] == True or col[j][val - 1] == True or  sub[box][val - 1] == True:
                        return False
                    else:
                        row[i][val - 1] = True 
                        col[j][val - 1] =  True  
                        sub[box][val - 1] = True
        return True


        
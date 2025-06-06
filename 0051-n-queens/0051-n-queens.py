class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessbroad = ['.' * n for _ in range(n)]
        rst = []
        self.backtracking(n,chessbroad,0,rst)
        return rst


    def backtracking(self,n,chessbroad,row,rst):
        if row == n:
            rst.append(chessbroad[:])
        for i in range(n):
            if self.isvalid(row,i,n,chessbroad):
                chessbroad[row] = chessbroad[row][:i] + "Q" + chessbroad[row][i+1:]
                self.backtracking(n,chessbroad,row + 1,rst)
                chessbroad[row] = chessbroad[row][:i] + "." + chessbroad[row][i+1:]
    def isvalid(self,row,col,n,chessbroad):
        for i in range(n):
            if chessbroad[i][col] == "Q":
                return False

        i ,j = row - 1 ,col - 1
        while i >= 0 and j >= 0:
            if chessbroad[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        
        i,j = row - 1, col + 1
        while j >= 0 and j < n:
            if chessbroad[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

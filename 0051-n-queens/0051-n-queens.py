class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def add_queens(queens):
            rst = []
            for _ , col in queens:
                level = '.'* col + 'Q' + '.'*(n - col - 1)
                rst.append(level)
            return rst


        if n == 1:
            return [['Q']]
        cols = set()
        dig1 = set()
        dig2 = set()
        rst = []
        queens = []
        def dfs(row):
            if row == n:
                rst.append(add_queens(queens))
            for col in range(n):
                if col in cols or row + col in dig1 or row - col in dig2:
                    continue
                cols.add(col)
                dig1.add(col + row)
                dig2.add(row - col)
                queens.append((row , col))
                dfs(row + 1)
                queens.pop()
                cols.remove(col)
                dig1.remove(col + row)
                dig2.remove(row - col)
        dfs(0)
        return rst

            




        


        
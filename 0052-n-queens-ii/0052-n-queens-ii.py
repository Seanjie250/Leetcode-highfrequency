class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()
        diag2 = set()
        ans = 0

        def backtracking(r):
            nonlocal ans
            if r == n:
                ans += 1
            for i in range(n):
                if i in cols or r - i in diag1 or r + i in diag2:
                    continue
                cols.add(i)
                diag1.add(r - i)
                diag2.add(r + i)

                backtracking(r + 1)
                
                cols.remove(i)
                diag1.remove(r - i)
                diag2.remove(r + i)
        backtracking(0)
        return ans

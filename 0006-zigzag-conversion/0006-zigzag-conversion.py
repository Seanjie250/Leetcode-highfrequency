class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        grid = [[''] * n for _ in range(numRows)]

        down = True
        j = 0
        for i in range(len(s)):
            ch = s[i]
            grid[j][i] = ch
            if down == True:
                j += 1
            else:
                j -= 1
            if j == numRows - 1:
                down = False
            elif j == 0:
                down = True
        return ''.join(''.join(row) for row in grid)
        
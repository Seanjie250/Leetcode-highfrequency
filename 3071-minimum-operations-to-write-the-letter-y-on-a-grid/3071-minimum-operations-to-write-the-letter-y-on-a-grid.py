class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        isY = [0 , 0 , 0]
        notY = [0 , 0 , 0]
        mid = n // 2
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if (i == j and  j <= mid) or (i + j == n - 1 and i <= mid) or (j == mid and i >= mid):
                    isY[v] += 1
                else:
                    notY[v] += 1
        print(isY , notY)

        sumisY = sum(isY)
        sumnotY = sum(notY)

        minm = float('inf')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                count = 0
                count += sumisY - isY[i]
                count += sumnotY - notY[j]
                minm = min(minm , count)
        return minm
                
            


       
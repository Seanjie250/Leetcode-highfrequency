class Solution:


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r , c = len(grid),len(grid[0])
        visited = [[False] * c for _ in range(r)]
        perimeter = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter




                    

 

        
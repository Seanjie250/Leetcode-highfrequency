class Solution:
    def dfs(self,heights,visited,x,y,side):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        if visited[x][y]:
            return 
        visited[x][y] = True
        side.add((x,y))
        for i,j in directions:
            next_x = x + i
            next_y = y + j
            if 0 <= next_x < len(heights) and 0 <= next_y < len(heights[0]) and  heights[next_x][next_y] >= heights[x][y]:
                self.dfs(heights,visited,next_x,next_y,side)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m ,n = len(heights) ,len(heights[0])
        first = set()
        second = set()

        visited = [[False] * n for _ in range(m)]
        for i in range(n):
            self.dfs(heights,visited,0,i,first)
        for i in range(m):
            self.dfs(heights,visited,i,0,first)

        visited = [[False] * n for _ in range(m)]
        for i in range(n):
            self.dfs(heights,visited,m - 1,i,second)
        for i in range(m):
            self.dfs(heights,visited,i,n - 1,second)

        rst = first & second

        return list(map(list, first & second))
        


        
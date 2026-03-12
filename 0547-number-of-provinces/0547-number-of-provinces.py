class UnionFind:
    def __init__(self , n):
        self.rank = [1] * n
        self.count = n
        self.parent = list(range(n))
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self , x , y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        self.count -= 1
class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        UF = UnionFind(n)
        for i in range(n):
            for j in range(i + 1 , n):
                if isConnected[i][j] == 1:
                    UF.union(i , j)
        return UF.count
        
class Solution:
    def backtracking(self,n,k,startIndex,path,rst):
        if len(path) == k:
            rst.append(path[:])
            return 
        for i in range(startIndex,n+1):
            path.append(i)
            self.backtracking(n,k,i + 1,path,rst)
            path.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        rst = []
        self.backtracking(n,k,1,[],rst)
        return rst
        
        
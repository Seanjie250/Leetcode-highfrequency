class Solution:
    def backtracking(self, k ,n ,startindex,rst, path):
        if sum(path) > n:
            return
        if len(path) == k and sum(path) == n:
            rst.append(path[:])
            return
        for i in range(startindex, 9 - (k - len(path)) + 2):
            path.append(i)
            self.backtracking(k,n,i + 1,rst,path)
            path.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        rst = []
        path = []
        self.backtracking(k,n,1,rst,path)

        return rst
        
        
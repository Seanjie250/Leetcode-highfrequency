class Solution:
    def backtracking(self, path ,rst , start , n , k):
        if sum(path) == n:
            if len(path) == k:
                rst.append(list(path))
        for i in range(start , 10):
            path.append(i)
            self.backtracking(path , rst, i + 1, n , k)
            path.pop()
        


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        rst = []
        path = []
        self.backtracking(path ,rst , 1 , n , k)
        return rst



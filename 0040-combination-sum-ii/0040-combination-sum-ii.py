class Solution:
    def backtracking(self,candidates,target,path,rst,startindex):
        if sum(path) > target:
            return
        if sum(path) == target:
            rst.append(path[:])
            return
        for i in range(startindex,len(candidates)):
            if candidates[i] == candidates[i - 1] and i > startindex:
                continue
            path.append(candidates[i])
            self.backtracking(candidates,target,path,rst,i + 1)
            path.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        rst = []
        path = []
        candidates.sort()
        self.backtracking(candidates,target,path,rst,0)
        return rst
        
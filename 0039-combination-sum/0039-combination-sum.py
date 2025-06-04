class Solution:
    def backtracking(self,startindex,path,rst,target,candidates):
        if sum(path) > target:
            return
        if sum(path) == target:
            rst.append(path[:])
            return
        for i in range(startindex,len(candidates)):
            path.append(candidates[i])
            self.backtracking(i,path,rst,target,candidates)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rst = []
        self.backtracking(0,[],rst,target,candidates)
        return rst

        
class Solution:
    def backtracking(self,nums,path,rst,used,startindex):
        if len(path) == len(nums):
            rst.append(path[:])
            return 
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums,path,rst,used,0)
            path.pop()
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        self.backtracking(nums,path,rst,[False]*len(nums),0)
        return rst
        
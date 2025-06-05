class Solution:
    def backtracking(self,nums,path,rst,startindex):
        rst.append(path[:])
        for i in range(startindex,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,path,rst,i + 1)
            path.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        self.backtracking(nums,path,rst,0)
        return rst
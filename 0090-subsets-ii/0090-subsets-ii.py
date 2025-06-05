class Solution:
    def backtracking(self,nums,path,rst,startindex):
        rst.append(path[:])
        if startindex >= len(nums):
            return 
        for i in range(startindex,len(nums)):
            if i > startindex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtracking(nums,path,rst,i + 1)
            path.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rst = []
        path = []
        self.backtracking(nums,path,rst,0)
        return rst

        
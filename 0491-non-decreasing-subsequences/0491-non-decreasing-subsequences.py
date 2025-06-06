class Solution:
    def backtracking(self,nums,path,rst,startindex):
        if len(path) > 1:
            rst.append(path[:])

        uset = set()
        for i in range(startindex,len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums,path,rst,i + 1)
            path.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        self.backtracking(nums,path,rst,0)
        return rst
        
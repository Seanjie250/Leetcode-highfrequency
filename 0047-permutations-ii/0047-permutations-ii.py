class Solution:
    def backtracking(self,nums,path,rst,used,uset):
        if len(path) == len(nums) and tuple(path) not in uset:
            uset.add(tuple(path))
            rst.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums,path,rst,used,uset)
            path.pop()
            used[i] = False
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        rst = []
        uset = set()
        used = [False] * len(nums)
        self.backtracking(nums,path,rst,used,uset)
        return rst        
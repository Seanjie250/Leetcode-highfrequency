class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        def dfs(i , path):
            rst.append(path.copy())
            for j in range(i , len(nums)):
                path.append(nums[j])
                dfs(j + 1 , path)
                path.pop()
        dfs(0 , path)
        return rst
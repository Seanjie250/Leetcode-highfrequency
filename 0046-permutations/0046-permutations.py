class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        visited = set()
        def dfs(path):
            if len(path) == len(nums):
                rst.append(path[:])
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    
                    dfs(path)
                    path.pop()
                    visited.remove(num)
        dfs(path)
        return rst
                    

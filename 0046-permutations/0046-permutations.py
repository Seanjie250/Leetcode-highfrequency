class Solution:
    def dfs(self , path , rst , nums , visited):
        if len(path) == len(nums) and path not in rst:
            rst.append(path[:])
        for num in nums:
            if num not in visited:
                visited.add(num)
                path.append(num)
                self.dfs(path , rst,  nums , visited)
                path.pop()
                visited.remove(num)
        return rst
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        visited = set()
        rst = self.dfs(path , rst,  nums ,visited)
        return rst

        
        
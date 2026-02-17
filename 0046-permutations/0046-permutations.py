class Solution:
    def backtracking(self , rst , path , visited , nums):
        if len(path) == len(nums):
            print(path)
            rst.append(list(path))
            return 
        for i in range(len(nums)):
            if visited[i] == True:
                continue
            path.append(nums[i])
            visited[i] = True
            self.backtracking(rst , path ,visited , nums)
            path.pop()
            visited[i] = False
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst = []
        path = []
        visited = [False] * len(nums) 
        self.backtracking(rst , path , visited, nums)
        return rst

        
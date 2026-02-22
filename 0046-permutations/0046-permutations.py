class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
        
            path = []
            rst = []
            visited = [False] * len(nums)
            def backtracking(path , rst):
                if len(path) == len(nums):
                    rst.append(list(path))
                    return
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = True
                        path.append(nums[i])
                        backtracking(path , rst)
                        path.pop()
                        visited[i] = False
            backtracking(path ,rst)
            return rst

            

        
        
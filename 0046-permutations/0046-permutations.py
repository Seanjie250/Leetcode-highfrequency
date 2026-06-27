class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        seen = set()
        rst = []
        def backtracking(path , seen):
            if len(path) == len(nums):
                rst.append(path[:])
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    path.append(num)
                    backtracking(path , seen)
                    seen.remove(num)
                    path.pop()
        backtracking(path , seen)
        return rst
        
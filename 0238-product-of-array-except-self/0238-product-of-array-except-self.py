class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rst = [1] * n
        prefix = 1
        for i in range(n):
            rst[i] = prefix
            prefix *= nums[i]
        
        subfix = 1
        for i in range(n -1 , - 1, -1):
            rst[i] *= subfix
            subfix *= nums[i]
        return rst

            


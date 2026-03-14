class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fix_l = [0] * len(nums)
        fix_l[0] = nums[0]
        fix_r = [0] * len(nums)
        fix_r[-1] = nums[-1]
        for i in range(1, len(nums)):
            fix_l[i] = fix_l[i - 1] * nums[i]     
        for i in range(len(nums) - 2 , -1 , -1):
            fix_r[i] = fix_r[i + 1] * nums[i] 
        rst = [0] * len(nums)
        rst[0] = fix_r[1]
        rst[-1] = fix_l[-2]
        for i in range(1 , len(nums) - 1):
            rst[i] = fix_l[i - 1] * fix_r[i + 1]
        return rst
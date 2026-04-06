class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        end = 0
        rst = 0
        for i in range(len(nums) - 1):
            far = max(i + nums[i] , far)
            if i == end:
                end = far
                rst += 1
        return rst
        
        
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        far = 0
        count = 0
        for i in range(len(nums) - 1):
            far = max(far , i + nums[i])
            
            if i == end:
                end = far
                count += 1
        return count

        
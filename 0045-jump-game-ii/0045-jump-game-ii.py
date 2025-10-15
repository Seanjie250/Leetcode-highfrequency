class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_pos = 0
        next_pos = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            next_pos = max(next_pos , nums[i] + i)
            if i == cur_pos:
                ans += 1
                cur_pos = next_pos
            if cur_pos >= len(nums) - 1:
                break
        return ans

 




        
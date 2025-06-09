class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_dis = 0
        next_dis = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums) - 1):
            next_dis = max(next_dis,nums[i] + i)
            if i == cur_dis:
                ans += 1
                cur_dis = next_dis
                if next_dis >= len(nums) - 1:
                    break
        return ans



        
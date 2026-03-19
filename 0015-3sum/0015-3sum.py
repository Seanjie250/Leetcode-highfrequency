class Solution:
    def twoSum(self , nums , target):
        rst  = []
        left , right = 0 , len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                rst.append([nums[left] , nums[right]])
                print(rst)
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return rst

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        rst = []
        seen = set()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            subset = self.twoSum(nums[i + 1 : ] , target)
            for sub in subset:
                rst.append([nums[i]] + sub)
        return rst


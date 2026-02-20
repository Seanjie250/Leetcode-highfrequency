class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        def findtwosum(nums , target):
            l , r = 0 , len(nums) - 1
            rst = []
            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ > target:
                    r -= 1
                elif sum_ < target:
                    l += 1
                elif sum_ == target:
                    rst.append([nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            return rst
    
        def kthsum(nums, k , target):
            avg = target / k
            rst = []
            if nums[0] > avg or nums[-1] < avg:
                return rst
            
            if k == 2:
                return findtwosum(nums,target)

            for i in range(len(nums) - k + 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                for subset in kthsum(nums[i + 1:] , k - 1 , target - nums[i]):
                    rst.append([nums[i]] + subset)
            return rst

        return kthsum(nums , 4, target)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        def find2sum(nums , target):
            left , right = 0 , len(nums) - 1
            rst = []
           
            while left < right:
                sum_ = nums[left] + nums[right]
                if sum_ > target:
                    right -= 1
                elif sum_ < target:
                    left += 1
                else:
                    rst.append([nums[left] , nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            print(rst)
            return rst
                    
        
        def kthsum(nums , target , k):
            avg = target / k
            rst = []
            if nums[0] > avg or nums[-1] < avg:
                return rst
            if k == 2:
                return find2sum(nums , target)
            for i in range(len(nums) - k + 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                for subset in kthsum(nums[i + 1:] , target - nums[i] , k - 1):
                    rst.append([nums[i]] + subset)
                    print(rst)
            return rst
        
        return kthsum(nums, target, 4)
                
            

        
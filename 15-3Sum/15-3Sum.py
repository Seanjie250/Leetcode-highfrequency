# Last updated: 5/18/2025, 2:56:22 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        record = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1 
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ > 0:
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    record.append([nums[i],nums[left],nums[right]])
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    while right > left and nums[left] == nums[left+1]:
                        left += 1
                    right -= 1
                    left += 1
        return record
                
            


                



        
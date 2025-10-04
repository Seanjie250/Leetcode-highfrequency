class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k , j = len(nums) - 1, len(nums) - 1
        i = 0
        result = [float('inf')] * len(nums)
        while k >= 0 :
            if nums[i] * nums[i] >= nums[j]*nums[j]:
                result[k] = nums[i] * nums[i]
                i += 1
            elif nums[i] * nums[i] < nums[j]*nums[j]:
                result[k] = nums[j] * nums[j]
                j -= 1
            k -= 1
        return result
                

        
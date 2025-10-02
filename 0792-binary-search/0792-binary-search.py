class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if n == 1:
            return 0 if nums[0] == target else -1
        if n == 0:
            return -1
        while left <= right:
            mid =( left + right )  // 2

            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] == target:
                return mid
        return -1

        
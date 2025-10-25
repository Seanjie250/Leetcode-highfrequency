class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        if len(nums) == 2:
            return True if nums[0] == nums[1] else False
        for i in range(len(nums) - 1):
            endpoint = min(len(nums) , i + k + 1)
            for j in range(i + 1 , endpoint):
                if nums[i] == nums[j]:
                    return True
        return False


        
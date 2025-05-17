# Last updated: 5/17/2025, 4:58:17 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for index , value in enumerate(nums):
            if target - value in record:
                return [index,record[target-value]]
            record[value] = index
        return []

        
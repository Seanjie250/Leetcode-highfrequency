class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        rst = []
        for index , num in enumerate(nums):
            if target - num in seen:
                index2 = seen[target - num]
                rst.append(index)
                rst.append(index2)
            seen[num] = index
        return rst

        
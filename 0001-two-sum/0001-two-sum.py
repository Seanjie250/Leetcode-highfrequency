class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for index , num in enumerate(nums):
            if target - num in seen:
                key = seen[target - num]
                return (index , key)
            else:
                seen[num] = index
        

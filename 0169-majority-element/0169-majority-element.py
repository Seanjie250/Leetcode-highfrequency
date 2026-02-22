class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for number , count in count.items():
            if count >= len(nums) / 2:
                return number
        
        
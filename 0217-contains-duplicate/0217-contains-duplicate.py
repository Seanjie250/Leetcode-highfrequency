class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for num , cot in count.items():
            if cot > 1:
                return True
        return False
# Last updated: 5/17/2025, 10:55:25 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

        
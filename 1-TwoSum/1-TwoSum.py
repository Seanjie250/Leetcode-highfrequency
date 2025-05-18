# Last updated: 5/18/2025, 9:51:03 AM
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1 + n2] += 1
                else:
                    hashmap[n1 + n2] = 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count

        
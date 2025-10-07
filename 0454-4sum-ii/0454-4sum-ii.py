class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        for i in nums1:
            for j in nums2:
                if i + j in hashmap:
                    hashmap[i + j] += 1
                else:
                    hashmap[i + j] = 1
        count = 0

        for i in nums3:
            for j in nums4:
                if - i - j in hashmap:
                    key = - i - j
                    count += hashmap[key]
        return count





        
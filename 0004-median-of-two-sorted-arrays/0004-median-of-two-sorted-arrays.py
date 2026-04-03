class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2 , nums1)
        l , r = 0 , len(nums1)
        while l <= r:
            pA = (l + r) // 2
            pB = (len(nums1) + len(nums2) + 1) // 2 - pA
            leftmaxA = nums1[pA - 1] if pA > 0 else float('-inf')
            rightminA = nums1[pA] if pA < len(nums1) else float('inf')
            leftmaxB = nums2[pB - 1] if pB > 0 else float('-inf')
            rightminB = nums2[pB] if pB < len(nums2) else float('inf')
            
            if leftmaxA <= rightminB and rightminA >= leftmaxB:
                if (len(nums1) + len(nums2)) % 2:
                    return float(max(leftmaxA  , leftmaxB))
                else:
                    return (max(leftmaxA  , leftmaxB) + min(rightminA , rightminB)) / 2.0
            else:
                if leftmaxA > rightminB:
                    r = pA - 1
                elif rightminA < leftmaxB:
                    l = pA + 1
            

        
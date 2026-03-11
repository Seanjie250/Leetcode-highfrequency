class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m + n - 1
        p2 = m - 1
        p3 = n - 1
        while p1 >= 0 and p2 >= 0 and p3 >= 0:
            if nums1[p2] >= nums2[p3]:
                nums1[p1] = nums1[p2]
                p2 -= 1
            else:
                nums1[p1] = nums2[p3]
                p3 -= 1
            p1 -= 1
        while p2 >= 0:
            return 
        while p3 >= 0:
            nums1[p1] = nums2[p3]
            p3 -= 1
            p1 -= 1
        

        
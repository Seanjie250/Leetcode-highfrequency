class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        rst = []

        min_heap = []
        for i in range(len(nums1)):
            heapq.heappush(min_heap,(nums1[i] + nums2[0],i,0))
        
        while k > 0 and min_heap:
            cur_sum , i ,j = heapq.heappop(min_heap)
            rst.append([nums1[i] , nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap , (nums1[i] + nums2[j + 1] , i , j + 1))
            k -= 1
        return rst


        
        
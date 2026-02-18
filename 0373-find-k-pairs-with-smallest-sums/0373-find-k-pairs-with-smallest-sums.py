import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        ans = []
        count = 0
        for i in range(len(nums1)):
            pq.append(((nums1[i] + nums2[0]) , nums1[i], nums2[0] , 0 ))
        heapq.heapify(pq)
        while pq and len(ans) < k:
            _ , num1 , num2 ,index = heapq.heappop(pq)
            ans.append([num1, num2])
            if index + 1 < len(nums2):
                heapq.heappush(pq , (num1 + nums2[index + 1] , num1 , nums2[index + 1] , index + 1))
            count += 1
            
        return ans
            


        
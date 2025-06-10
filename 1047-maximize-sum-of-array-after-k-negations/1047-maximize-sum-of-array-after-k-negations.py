class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            minm = heapq.heappop(nums)      
            heapq.heappush(nums,-minm)
        return sum(nums)



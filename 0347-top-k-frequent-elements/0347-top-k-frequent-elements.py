class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        res = []
        for num , count in counter.items():
            heap.append((-count , num))
        heapq.heapify(heap)

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        rst = []
        for num , index in count.items():
            print(num)
            print(index)
            heapq.heappush(heap , (- index , num))
        top_k = 0
        while top_k < k:
            index , num = heapq.heappop(heap)
            rst.append(num) 
            top_k += 1
        return rst           
            
        
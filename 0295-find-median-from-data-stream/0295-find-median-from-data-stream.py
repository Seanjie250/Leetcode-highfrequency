class MedianFinder:
    def __init__(self):
        self.large = []
        self.small = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.large , num)
        num = heapq.heappop(self.large)
        heapq.heappush(self.small , -num)
        if len(self.small) > len(self.large):
            x = heapq.heappop(self.small)
            heapq.heappush(self.large , -x)
    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        if not intervals:
            return []
        rst = [intervals[0]]
        for interval in intervals[1:]:
            if rst[-1][1] >= interval[0]:
                rst[-1][0] = min(interval[0] , rst[-1][0])
                rst[-1][1] = max(interval[1] , rst[-1][1])
            else:
                rst.append(interval)
        return rst
                
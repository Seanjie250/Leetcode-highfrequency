class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals , key = lambda x : x[0])
        rst = []
        rst.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] <= rst[-1][1]:
                rst[-1][0] = min(interval[0] , rst[-1][0])
                rst[-1][1] = max(interval[1] , rst[-1][1])
            else:
                rst.append(interval)
        return rst
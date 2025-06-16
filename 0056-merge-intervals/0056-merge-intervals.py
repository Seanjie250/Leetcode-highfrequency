class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        rst = []
        rst.append(intervals[0])
        for interval in intervals[1:]:
            prev = rst[-1]
            if prev[1] >= interval[0]:
                prev[1] = max(interval[1],prev[1])
            else:
                rst.append(interval)

        return rst

        
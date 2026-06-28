class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals , key = lambda x : x[0])
        rst = []
        rst.append(intervals[0])
        for start , end in intervals[1:]:
            if rst and start <= rst[-1][1]:
                rst[-1][1] = max(end , rst[-1][1])
            else:
                rst.append([start , end])

        return rst
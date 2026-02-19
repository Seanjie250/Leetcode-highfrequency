class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        if len(intervals) == 1:
            return intervals
        rst = [intervals[0]]
        for i in range(1 , len(intervals)):
            if rst[-1][1] >= intervals[i][0]:
                rst[-1][0] = min(rst[-1][0] , intervals[i][0])
                rst[-1][1] = max(rst[-1][1] , intervals[i][1])
            else:
                rst.append(intervals[i])
                continue
        return rst 
        
        
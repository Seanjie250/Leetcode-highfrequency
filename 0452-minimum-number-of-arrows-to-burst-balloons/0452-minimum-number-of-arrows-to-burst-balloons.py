class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        n = len(points)
        count = 1
        cur = points[0]
        if len(points) == 1:
            return 1

        for start , end in points[1:]:
            if cur[1] >= start:
                start = max(cur[0] , start)
                end = min(cur[1] , end)
                cur = [start , end]
            else:
                count += 1
                cur = [start , end]
        return count        